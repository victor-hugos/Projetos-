import requests
import json
import os
from pipeline_unificado import fetch_document_comments, headers_outline, OUTLINE_BASE_URL

# ID de um documento para teste (ex: DAIA)
TEST_DOC_ID = "d637f7b0-fb1f-485e-88dd-770ae7704e6c" 

def save_debug_json(doc_id):
    print(f"Baixando dados brutos do documento {doc_id}...")
    
    # 1. Info do Documento
    res = requests.post(
        f"{OUTLINE_BASE_URL}/documents.info", 
        json={"id": doc_id}, 
        headers=headers_outline
    )
    
    if res.status_code != 200:
        print(f"Erro ao baixar documento: {res.status_code}")
        return

    doc_data = res.json().get('data', {})
    title = doc_data.get('title', 'Sem Título')
    
    # 2. Comentários
    comments = fetch_document_comments(doc_id, title)
    
    # 3. Montar o objeto JSON completo (igual ao que o pipeline usa)
    # Simulando um path para o exemplo
    full_data = {
        "id": doc_id,
        "title": title,
        "path": "Coleção Exemplo > Caminho > " + title,
        "text": doc_data.get('text', ''),
        "updatedAt": doc_data.get('updatedAt', ''),
        "comments": comments,
        "raw_metadata": doc_data # Incluindo metadados extras do Outline para inspeção
    }
    
    # 4. Salvar em arquivo
    filename = "exemplo_estrutura_completa.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(full_data, f, indent=2, ensure_ascii=False)
        
    print(f"✅ Sucesso! Arquivo JSON salvo em: {os.path.abspath(filename)}")
    print("Este arquivo contém exatamente a estrutura que é passada para o gerador de Markdown.")

if __name__ == "__main__":
    save_debug_json(TEST_DOC_ID)
