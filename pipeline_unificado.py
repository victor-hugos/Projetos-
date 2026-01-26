"""
Script de orquestração do Pipeline Unificado.

Este script é responsável por automatizar todo o ciclo de vida da ingestão de documentos
da Outline Wiki para a Base de Conhecimento (Knowledge Base).

Fluxo de Execução:
1. Conecta à API do Outline e lista todas as coleções disponíveis.
2. Para cada coleção, cria uma pasta local correspondente.
3. Navega recursivamente pela árvore de documentos de cada coleção.
4. Baixa o conteúdo Markdown de cada documento.
5. Invoca o `KnowledgeBaseService` para processar, fragmentar e indexar os arquivos.

Uso:
    python pipeline_unificado.py
"""

import os
import requests
import json
from typing import Dict, Any, List
from formataçao_de_chunks import KnowledgeBaseService, BASE_DIR
from outline_transformer import transform_to_rag_markdown

# --- CONFIGURAÇÕES DO OUTLINE ---
# Nota: Em produção, recomenda-se usar variáveis de ambiente para a API KEY.
OUTLINE_API_KEY = "ol_api_8SNMXz3Qgx4AuuT8tlkUEymeXJ7dJATBeQ8Vbc"
OUTLINE_BASE_URL = "https://portal.zello.space/api"

headers_outline = {
    "Authorization": f"Bearer {OUTLINE_API_KEY}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

def fetch_document_comments(doc_id: str, doc_title: str) -> List[Dict[str, Any]]:
    """
    Busca os comentários de um documento específico na API do Outline.
    
    Args:
        doc_id (str): ID do documento.
        doc_title (str): Título do documento (para logs).
        
    Returns:
        List[Dict[str, Any]]: Lista de comentários processados.
    """
    try:
        res = requests.post(
            f"{OUTLINE_BASE_URL}/comments.list", 
            json={"documentId": doc_id, "limit": 100}, 
            headers=headers_outline
        )
        
        if res.status_code == 200:
            raw_comments = res.json().get('data', [])
            processed_comments = []
            
            for comm in raw_comments:
                # Extração segura de campos
                created_by = comm.get('createdBy', {})
                user_name = created_by.get('name', 'Desconhecido') if isinstance(created_by, dict) else 'Desconhecido'
                
                # Tenta identificar a seção ou contexto (ainda experimental sem docs exata)
                # A API pode retornar 'quoted' ou 'context' dependendo da versão
                section_context = "Geral / Não especificado"
                
                # Processa o comentário
                # O conteúdo do comentário no Outline geralmente vem no campo 'data'
                # Pode ser texto simples ou estrutura Prosemirror
                raw_content = comm.get('data', '')
                
                # Se for um dicionário (Prosemirror), tentamos extrair texto simplificado
                # Por enquanto, salvamos como string para garantir
                content_str = str(raw_content)
                
                processed_comments.append({
                    "data_criacao": comm.get('createdAt'),
                    "user": user_name,
                    "comentario": content_str,
                    "secao_origem": section_context,
                    "raw_id": comm.get('id')
                })
            
            if processed_comments:
                print(f"   [Info] {len(processed_comments)} comentários encontrados em '{doc_title}'.")
            
            return processed_comments
            
        else:
            # print(f"   [Aviso] Não foi possível buscar comentários para '{doc_title}': {res.status_code}")
            return []
            
    except Exception as e:
        print(f"   [Erro] Falha ao buscar comentários de '{doc_title}': {e}")
        return []

def download_node_recursive(node: Dict[str, Any], parent_dir: str, breadcrumb_prefix: str) -> None:
    """
    Percorre a árvore de documentos recursivamente e baixa o conteúdo para o disco local.
    
    Esta função lida com a estrutura hierárquica do Outline, onde documentos podem
    ter "filhos" (sub-documentos). Atualmente, ela "achata" a estrutura de arquivos
    dentro da pasta da coleção, mas preserva a lógica de navegação.

    Args:
        node (Dict[str, Any]): Dicionário representando um nó (documento) da árvore do Outline.
        parent_dir (str): Caminho do diretório local onde o arquivo deve ser salvo.
        breadcrumb_prefix (str): Prefixo do caminho hierárquico (ex: "Coleção > Pai").
    """
    doc_id = node.get('id')
    title = node.get('title', 'Sem Título')
    children = node.get('children', [])
    
    # Constrói o breadcrumb atual
    current_path = f"{breadcrumb_prefix} > {title}"
    
    # Cria nome seguro para arquivo (ex: "Manual de Uso" -> "manual-de-uso.md")
    safe_name = KnowledgeBaseService.slugify(title)
    
    # 1. Baixar o documento atual
    if doc_id:
        try:
            # print(f"   Baixando: {title}...") # Verbose opcional
            info_res = requests.post(
                f"{OUTLINE_BASE_URL}/documents.info", 
                json={"id": doc_id}, 
                headers=headers_outline
            )
            
            if info_res.status_code == 200:
                doc_data = info_res.json().get('data', {})
                conteudo = doc_data.get('text', '')
                updated_at = doc_data.get('updatedAt', '')
                
                # 1.1 Baixar comentários
                comments = fetch_document_comments(doc_id, title)
                
                # 1.2 Montar objeto unificado para transformação
                full_data = {
                    "id": doc_id,
                    "title": title,
                    "path": current_path,
                    "text": conteudo,
                    "updatedAt": updated_at,
                    "comments": comments
                }
                
                # 1.3 Transformar em Markdown Otimizado (RAG)
                markdown_content = transform_to_rag_markdown(full_data)
                
                # Salva o arquivo único transformado
                filename = f"{safe_name}.md"
                filepath = os.path.join(parent_dir, filename)
                
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(markdown_content)
                        
            else:
                print(f"   [Erro] Falha ao baixar '{title}': {info_res.status_code}")
                
        except Exception as e:
            print(f"   [Erro] Exceção ao baixar '{title}': {e}")

    # 2. Processar filhos (se houver) recursivamente
    if children:
        # Nota: Se desejar criar subpastas reais no sistema de arquivos para
        # refletir a hierarquia do Outline, descomente o bloco abaixo:
        #
        # sub_dir = os.path.join(parent_dir, safe_name)
        # if not os.path.exists(sub_dir):
        #     os.makedirs(sub_dir)
        # parent_dir = sub_dir
        
        for child in children:
            download_node_recursive(child, parent_dir, current_path)

def sync_all_collections() -> None:
    """
    Sincroniza todas as coleções do Outline com o sistema de arquivos local.
    
    1. Lista todas as coleções visíveis para a chave de API.
    2. Cria diretórios correspondentes em `DAIA_Markdown/`.
    3. Baixa todos os documentos de cada coleção.
    """
    print("--- 1. INICIANDO DOWNLOAD DE TODAS AS COLEÇÕES ---")
    
    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)

    try:
        # 1. Listar todas as coleções
        res = requests.post(
            f"{OUTLINE_BASE_URL}/collections.list", 
            json={}, 
            headers=headers_outline
        )
        
        if res.status_code != 200:
            print(f"Erro fatal ao listar coleções: {res.status_code}")
            return

        collections = res.json().get('data', [])
        print(f"Encontradas {len(collections)} coleções.")

        for col in collections:
            col_name = col['name']
            col_id = col['id']
            
            print(f"\n📂 Processando Coleção: {col_name}")
            
            # Criar pasta local para a coleção
            safe_col_name = KnowledgeBaseService.slugify(col_name)
            col_dir = os.path.join(BASE_DIR, safe_col_name)
            
            if not os.path.exists(col_dir):
                os.makedirs(col_dir)
            
            # 2. Obter árvore de documentos da coleção
            res_tree = requests.post(
                f"{OUTLINE_BASE_URL}/collections.documents", 
                json={"id": col_id}, 
                headers=headers_outline
            )
            
            if res_tree.status_code == 200:
                tree_nodes = res_tree.json().get('data', [])
                print(f"   Estrutura obtida. Iniciando download de {len(tree_nodes)} nós raiz...")
                
                for node in tree_nodes:
                    # O breadcrumb inicial é o nome da coleção
                    download_node_recursive(node, col_dir, col_name)
            else:
                print(f"   Erro ao obter documentos da coleção: {res_tree.status_code}")

    except Exception as e:
        print(f"Erro crítico no processo de download: {e}")

def run_pipeline() -> None:
    """
    Função principal que orquestra todo o pipeline.
    
    Etapas:
    1. sync_all_collections(): Baixa dados novos.
    2. KnowledgeBaseService.update_knowledge_base(): Processa e indexa.
    """
    # Passo 1: Download e Organização
    sync_all_collections()
    
    # Passo 2: Processamento Unificado
    print("\n--- 2. INICIANDO PROCESSAMENTO (CHUNKING & INGESTÃO) ---")
    # Nota: Não é necessário instanciar a classe pois os métodos são estáticos,
    # mas mantemos a chamada sem instância para clareza.
    resultado = KnowledgeBaseService.update_knowledge_base()
    print(f"\nRELATÓRIO FINAL:\n{resultado}")

if __name__ == "__main__":
    run_pipeline()
