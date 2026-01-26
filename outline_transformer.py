import json
from typing import Dict, Any, List

def transform_to_rag_markdown(data: Dict[str, Any]) -> str:
    """
    Transforma dados brutos do Outline em Markdown otimizado para RAG.
    
    Espera um dicionário com chaves:
    - id: str
    - title: str
    - path: str (breadcrumb separado por " > ")
    - text: str
    - updatedAt: str (ISO 8601)
    - comments: List[Dict]
    """
    
    # 1. Metadados (Frontmatter)
    page_id = data.get('id', '')
    path = data.get('path', '')
    updated_at = data.get('updatedAt', '')
    title = data.get('title', 'Sem Título')
    
    # Header YAML
    markdown = "---\n"
    markdown += f"id: {page_id}\n"
    markdown += f"path: {path}\n"
    markdown += f"updated_at: {updated_at}\n"
    markdown += "source: outline\n"
    markdown += "type: page\n"
    markdown += "---\n\n"
    
    # 2. Título e Conteúdo
    markdown += f"# {title}\n\n"
    markdown += "## 📄 Conteúdo da Página\n"
    
    content = data.get('text', '') or ''
    # Garantir que não haja espaços excessivos no início/fim, mas manter formatação interna
    markdown += content.strip() + "\n\n"
    
    # Separador
    markdown += "---\n\n"
    
    # 3. Comentários
    markdown += "## 💬 Comentários\n\n"
    
    comments = data.get('comments', [])
    
    if not comments:
        # Opcional: Se não houver comentários, pode deixar vazio ou colocar um aviso.
        # A estrutura pede "(Repetir bloco para cada comentário)", então se lista vazia, nada a repetir.
        pass
    else:
        for comment in comments:
            author = comment.get('user', 'Desconhecido')
            date = comment.get('data_criacao', '') # Usando a chave que vi no pipeline_unificado.py
            comment_text = comment.get('comentario', '').strip()
            
            # Formatação do bloco de comentário
            markdown += "### Comentário\n"
            markdown += f"- Autor: {author}\n"
            markdown += f"- Data: {date}\n"
            markdown += f"- Página: {path}\n\n"
            markdown += f"{comment_text}\n\n"
            
    return markdown
