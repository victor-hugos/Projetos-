"""
Módulo responsável pelo processamento, limpeza e fragmentação (chunking) de documentos Markdown.

Este módulo implementa o serviço KnowledgeBaseService, que prepara os documentos para
ingestão em um banco de dados vetorial (Vector DB). Ele utiliza técnicas de chunking
semântico, respeitando a hierarquia de títulos do Markdown (#, ##, ###) para preservar
o contexto.

Classes:
    Chunk: Dataclass que representa um fragmento de texto com metadados.
    KnowledgeBaseService: Classe principal contendo a lógica de processamento.
"""

import os
import re
import hashlib
import requests
from dataclasses import dataclass
from typing import List, Optional, Dict, Any, Generator, Tuple

# --- Configurações Gerais ---
# Se não houver variáveis de ambiente, usamos valores padrão ou vazios
MAX_CHARS_PER_CHUNK = 1500  # ~ 512 tokens
BASE_DIR = "DAIA_Markdown"   # Diretório base unificado

# Configurações de API (Vector DB)
VECTOR_INGEST_URL = os.getenv("VECTOR_INGEST_URL", "http://localhost:8000/ingest") 
VECTOR_DELETE_COLLECTION_URL = os.getenv("VECTOR_DELETE_COLLECTION_URL", "http://localhost:8000/delete_collection")
VECTOR_SEARCH_URL = os.getenv("VECTOR_SEARCH_URL", "http://localhost:8000/search")
VECTOR_COLLECTION_NAME = os.getenv("VECTOR_COLLECTION", "zello-knowledge-base")
API_KEY = os.getenv("LLM_API_KEY", "")

# Regex para identificar cabeçalhos Markdown (ex: # Título)
HEADER_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")

@dataclass
class Chunk:
    """
    Representa um fragmento de texto processado pronto para indexação.

    Attributes:
        chunk_id (str): Identificador único e estável do chunk.
        content (str): O conteúdo textual do chunk.
        metadata (Dict[str, Any]): Dicionário de metadados associados (ex: origem, seção).
    """
    chunk_id: str
    content: str
    metadata: Dict[str, Any]

class KnowledgeBaseService:
    """
    Serviço avançado para processamento de Base de Conhecimento (Knowledge Base).
    
    Principais funcionalidades:
    1. Chunking Semântico: Respeita a estrutura do Markdown (h1, h2, h3).
    2. Metadados Ricos: Extrai título, seção, subseção e hierarquia.
    3. Identificadores Estáveis: Gera IDs determinísticos baseados no conteúdo.
    4. Recursividade: Processa arquivos em subpastas automaticamente.
    """

    @staticmethod
    def slugify(text: str) -> str:
        """
        Converte uma string em um slug URL-friendly.
        
        Args:
            text (str): O texto original (ex: "Título do Documento").
            
        Returns:
            str: O texto normalizado (ex: "titulo-do-documento").
        """
        text = text.strip().lower()
        # Remove caracteres especiais mantendo unicode
        text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
        # Substitui espaços e underscores por hífens
        text = re.sub(r"[\s_-]+", "-", text)
        return text[:80] if text else "sem-titulo"

    @staticmethod
    def stable_id(*parts: str) -> str:
        """
        Gera um hash SHA1 determinístico a partir das partes fornecidas.
        Útil para criar IDs que não mudam se o conteúdo for o mesmo.
        
        Args:
            *parts: Componentes variáveis para compor o ID (ex: caminho, seção, texto).
            
        Returns:
            str: Hash SHA1 hexadecimal.
        """
        raw = "||".join(str(p) for p in parts if p is not None)
        return hashlib.sha1(raw.encode("utf-8")).hexdigest()

    @staticmethod
    def normalize_text(s: str) -> str:
        """
        Limpa e normaliza o texto removendo caracteres invisíveis e padronizando quebras de linha.
        
        Args:
            s (str): Texto bruto.
            
        Returns:
            str: Texto limpo e normalizado.
        """
        s = s.replace("\r\n", "\n").replace("\r", "\n")
        s = s.replace("\u00A0", " ").replace("\ufeff", "")
        s = s.replace("\u2028", "\n").replace("\u2029", "\n")
        # Remove caracteres de controle ASCII/Unicode indesejados
        s = re.sub(r"[\x00-\x08\x0B\x0C\x0E-\x1F]", " ", s)
        s = re.sub(r"[ \t\u200B\u200C\u200D\u2060]+", " ", s)
        # Limita quebras de linha consecutivas a 2 (parágrafos)
        s = re.sub(r"\n{3,}", "\n\n", s)
        return s.strip()

    @staticmethod
    def split_big_text_by_paragraph(text: str, max_chars: int) -> List[str]:
        """
        Divide um texto grande em blocos menores, tentando não quebrar parágrafos ao meio.
        
        Args:
            text (str): Texto completo a ser dividido.
            max_chars (int): Limite máximo de caracteres por bloco.
            
        Returns:
            List[str]: Lista de blocos de texto.
        """
        text = KnowledgeBaseService.normalize_text(text)
        if len(text) <= max_chars:
            return [text] if text else []

        paras = [p.strip() for p in text.split("\n\n") if p.strip()]
        out = []
        buf = []
        size = 0

        for p in paras:
            # Verifica se o parágrafo cabe no buffer atual
            if size + len(p) + (2 if buf else 0) <= max_chars:
                buf.append(p)
                size += len(p) + (2 if buf else 0)
            else:
                # Se não couber, descarrega o buffer
                if buf:
                    out.append("\n\n".join(buf).strip())
                
                # Inicia novo buffer com o parágrafo atual
                buf = [p]
                size = len(p)
                
                # Se o parágrafo sozinho já for maior que o limite, força a quebra
                if size > max_chars:
                    chunked = [p[i:i+max_chars] for i in range(0, len(p), max_chars)]
                    out.extend([c.strip() for c in chunked if c.strip()])
                    buf = []
                    size = 0

        if buf:
            out.append("\n\n".join(buf).strip())

        return out

    @staticmethod
    def remove_frontmatter(md: str) -> str:
        """
        Remove o bloco de frontmatter YAML do início do Markdown, se existir.
        
        Args:
            md (str): Texto Markdown original.
            
        Returns:
            str: Texto sem o frontmatter.
        """
        # Remove bloco entre --- e --- no início do arquivo
        return re.sub(r"^---\n.*?\n---\n", "", md, flags=re.DOTALL | re.MULTILINE)

    @staticmethod
    def parse_markdown_sections(md: str) -> Dict[str, Any]:
        """
        Analisa a estrutura do Markdown para extrair seções hierárquicas.
        
        Args:
            md (str): Conteúdo do arquivo Markdown.
            
        Returns:
            Dict[str, Any]: Estrutura contendo 'doc_title', 'intro_text' e lista de 'sections'.
        """
        # Remove frontmatter antes de processar
        md = KnowledgeBaseService.remove_frontmatter(md)
        
        md = md.replace("\r\n", "\n").replace("\r", "\n")
        lines = md.split("\n")

        doc_title: Optional[str] = None
        current_h2: Optional[str] = None
        current_h2_buf: List[str] = []
        current_h3: Optional[str] = None
        current_h3_buf: List[str] = []
        intro_buf: List[str] = []
        sections: List[Dict[str, Any]] = []
        current_section: Optional[Dict[str, Any]] = None

        def flush_h3():
            nonlocal current_h3, current_h3_buf, current_section
            if current_section is None:
                return
            if current_h3 is not None:
                text = KnowledgeBaseService.normalize_text("\n".join(current_h3_buf))
                current_section["sub"].append({
                    "h3_title": current_h3,
                    "h3_text": text
                })
            current_h3 = None
            current_h3_buf = []

        def flush_h2():
            nonlocal current_h2, current_h2_buf, sections, current_section
            if current_h2 is None:
                return
            flush_h3()
            if current_section is not None:
                text = KnowledgeBaseService.normalize_text("\n".join(current_h2_buf))
                current_section["h2_text"] = text
                sections.append(current_section)
            current_h2 = None
            current_h2_buf = []
            current_section = None

        for line in lines:
            m = HEADER_RE.match(line)
            if m:
                level = len(m.group(1))
                title = m.group(2).strip()
                title = KnowledgeBaseService.normalize_text(title)

                if level == 1 and doc_title is None:
                    doc_title = title
                    continue

                if level == 2:
                    flush_h2()
                    current_h2 = title
                    current_section = {"h2_title": title, "h2_text": "", "sub": []}
                    continue

                if level == 3:
                    if current_h2 is None:
                        intro_buf.append(line)
                        continue
                    flush_h3()
                    current_h3 = title
                    current_h3_buf = []
                    continue

            if current_h2 is None:
                intro_buf.append(line)
            else:
                if current_h3 is None:
                    current_h2_buf.append(line)
                else:
                    current_h3_buf.append(line)

        flush_h2()

        return {
            "doc_title": doc_title or "Sem título",
            "intro_text": KnowledgeBaseService.normalize_text("\n".join(intro_buf)),
            "sections": sections
        }

    @staticmethod
    def build_chunks_for_file(filepath: str, relpath: str, md: str) -> List[Chunk]:
        """
        Gera objetos Chunk a partir de um arquivo Markdown, preservando metadados hierárquicos.
        
        Args:
            filepath (str): Caminho absoluto do arquivo.
            relpath (str): Caminho relativo (usado nos metadados).
            md (str): Conteúdo do arquivo.
            
        Returns:
            List[Chunk]: Lista de chunks gerados.
        """
        parsed = KnowledgeBaseService.parse_markdown_sections(md)
        doc_title = parsed["doc_title"]
        intro_text = parsed["intro_text"]
        sections = parsed["sections"]

        chunks: List[Chunk] = []

        # --- 1. Chunks de Introdução (antes do primeiro H2) ---
        if intro_text:
            full_intro = f"{doc_title}\n\nIntrodução\n{intro_text}".strip()
            parts = KnowledgeBaseService.split_big_text_by_paragraph(full_intro, MAX_CHARS_PER_CHUNK)
            
            for i, part in enumerate(parts, start=1):
                cid = KnowledgeBaseService.stable_id(relpath, "intro", f"part:{i}", part[:200])
                chunks.append(Chunk(
                    chunk_id=cid,
                    content=part,
                    metadata={
                        "arquivo": relpath,
                        "documento": doc_title,
                        "secao": "Introdução",
                        "subsecao": None,
                        "nivel": 1,
                        "parte": i if len(parts) > 1 else None,
                        "path": relpath,
                        "source_type": "markdown",
                    }
                ))

        # --- 2. Fallback: Documento sem seções claras ---
        if not sections and not intro_text:
            text = KnowledgeBaseService.normalize_text(md)
            if text:
                cid = KnowledgeBaseService.stable_id(relpath, "full", text[:200])
                chunks.append(Chunk(
                    chunk_id=cid,
                    content=text,
                    metadata={
                        "arquivo": relpath,
                        "documento": doc_title,
                        "secao": "Conteúdo geral",
                        "subsecao": None,
                        "nivel": 0,
                        "path": relpath,
                        "source_type": "markdown",
                    }
                ))
            return chunks

        # --- 3. Chunks por Seção (H2/H3) ---
        for sec in sections:
            h2 = sec["h2_title"]
            h2_text = sec.get("h2_text", "") or ""
            subs = sec.get("sub", []) or []

            if subs:
                base_context = h2_text if h2_text else ""
                for sub in subs:
                    h3 = sub["h3_title"]
                    h3_text = sub.get("h3_text", "") or ""
                    # Constrói contexto: Título Doc > Título H2 > Título H3
                    full = f"{doc_title}\n\n{h2}\n"
                    if base_context:
                        full += f"{base_context}\n\n"
                    full += f"{h3}\n{h3_text}".strip()
                    full = KnowledgeBaseService.normalize_text(full)

                    parts = KnowledgeBaseService.split_big_text_by_paragraph(full, MAX_CHARS_PER_CHUNK)
                    for i, part in enumerate(parts, start=1):
                        cid = KnowledgeBaseService.stable_id(relpath, h2, h3, f"part:{i}", part[:200])
                        chunks.append(Chunk(
                            chunk_id=cid,
                            content=part,
                            metadata={
                                "arquivo": relpath,
                                "documento": doc_title,
                                "secao": h2,
                                "subsecao": h3,
                                "nivel": 3,
                                "parte": i if len(parts) > 1 else None,
                                "path": relpath,
                                "source_type": "markdown",
                            }
                        ))
            else:
                # Apenas H2
                full = f"{doc_title}\n\n{h2}\n{h2_text}".strip()
                full = KnowledgeBaseService.normalize_text(full)
                parts = KnowledgeBaseService.split_big_text_by_paragraph(full, MAX_CHARS_PER_CHUNK)
                for i, part in enumerate(parts, start=1):
                    cid = KnowledgeBaseService.stable_id(relpath, h2, f"part:{i}", part[:200])
                    chunks.append(Chunk(
                        chunk_id=cid,
                        content=part,
                        metadata={
                            "arquivo": relpath,
                            "documento": doc_title,
                            "secao": h2,
                            "subsecao": None,
                            "nivel": 2,
                            "parte": i if len(parts) > 1 else None,
                            "path": relpath,
                            "source_type": "markdown",
                        }
                    ))
        return chunks

    @staticmethod
    def iter_markdown_files(base_dir: str) -> Generator[Tuple[str, str], None, None]:
        """
        Itera recursivamente sobre arquivos .md em todas as subpastas.
        
        Args:
            base_dir (str): Diretório raiz para busca.
            
        Yields:
            Tuple[str, str]: (caminho_absoluto, caminho_relativo)
        """
        for root, _, files in os.walk(base_dir):
            for fn in files:
                if fn.lower().endswith(".md"):
                    full = os.path.join(root, fn)
                    rel = os.path.relpath(full, base_dir).replace("\\", "/")
                    yield full, rel

    @staticmethod
    def update_knowledge_base() -> str:
        """
        Executa o processo de ingestão completo: Leitura -> Chunking -> (Simulação) Envio.
        
        Returns:
            str: Relatório final da execução.
        """
        print(f"--- Iniciando Processamento (Base: {BASE_DIR}) ---", flush=True)
        
        if not os.path.exists(BASE_DIR):
             print(f"Diretório {BASE_DIR} não encontrado.")
             return "Falha: Diretório não existe"

        total_files = 0
        total_chunks = 0
        errors = 0

        # Iterar sobre todos os arquivos recursivamente
        for fullpath, relpath in KnowledgeBaseService.iter_markdown_files(BASE_DIR):
            try:
                with open(fullpath, "r", encoding="utf-8", errors="replace") as f:
                    md = f.read()
            
                chunks = KnowledgeBaseService.build_chunks_for_file(fullpath, relpath, md)
                
                if not chunks:
                    continue

                # Aqui simularíamos o envio para o Vector DB
                KnowledgeBaseService.send_to_vector_db(chunks, relpath)
                
                # Para feedback visual no terminal:
                # print(f"   -> Processado: {relpath} ({len(chunks)} chunks)")

                total_files += 1
                total_chunks += len(chunks)
                
            except Exception as e:
                print(f"Erro ao processar {relpath}: {e}")
                errors += 1

        return f"Concluído: {total_files} arquivos, {total_chunks} chunks gerados, {errors} erros."

    @staticmethod
    def send_to_vector_db(chunks: List[Chunk], filename: str) -> None:
        """
        Simula o envio dos chunks para um banco de vetores.
        
        Args:
            chunks (List[Chunk]): Lista de chunks a serem enviados.
            filename (str): Nome do arquivo de origem para log.
        """
        print(f"      [Simulação] Enviando {len(chunks)} chunks de {filename} para {VECTOR_COLLECTION_NAME}...")
