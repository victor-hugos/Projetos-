import requests
import os
import json

# --- CONFIGURAÇÕES ---
API_KEY = "ol_api_8SNMXz3Qgx4AuuT8tlkUEymeXJ7dJATBeQ8Vbc"
BASE_URL = "https://portal.zello.space/api"

# Estratégia: Usar a árvore da Coleção "Especialistas" para achar o "DAIA" e seus filhos
# pois documents.list retornou 401 (Não Autorizado) para este token.
COLLECTION_ID = "00422479-60ba-4e6d-ae04-c5f9f1d5431a" # ID da Coleção "Especialistas"
TARGET_DOC_ID = "d637f7b0-fb1f-485e-88dd-770ae7704e6c" # ID do Documento "DAIA"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

def find_node_recursive(nodes, target_id):
    for node in nodes:
        if node['id'] == target_id:
            return node
        if 'children' in node and node['children']:
            found = find_node_recursive(node['children'], target_id)
            if found:
                return found
    return None

def extrair_daia():
    print(f"📡 Conectando a {BASE_URL}...")
    
    # 1. BUSCAR A ESTRUTURA DA COLEÇÃO (TREE)
    print(f"📂 Buscando árvore da coleção Especialistas ({COLLECTION_ID})...")
    
    try:
        # Usamos collections.documents pois é o endpoint que sabemos que funciona (Status 200)
        response = requests.post(f"{BASE_URL}/collections.documents", json={"id": COLLECTION_ID}, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao buscar coleção: {e}")
        if response.status_code == 401:
            print("💡 Dica: Verifique a API Key.")
        return

    tree_data = response.json().get('data', [])
    
    # 2. ENCONTRAR O NÓ "DAIA" NA ÁRVORE
    print(f"🔍 Procurando documento 'DAIA' ({TARGET_DOC_ID}) na árvore...")
    daia_node = find_node_recursive(tree_data, TARGET_DOC_ID)
    
    if not daia_node:
        print("❌ Documento DAIA não encontrado na coleção Especialistas.")
        return

    print(f"✅ Encontrado: {daia_node['title']}")
    
    children = daia_node.get('children', [])
    print(f"📚 Documentos filhos encontrados: {len(children)}")
    
    if not children:
        print("⚠️ A pasta DAIA está vazia.")
        return

    # Criar pasta para salvar os arquivos
    output_dir = 'DAIA_Markdown'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 3. BAIXAR CONTEÚDO DE CADA FILHO
    sucessos = 0
    erros = 0

    for child in children:
        doc_id = child['id']
        doc_title = child['title']
        
        # Limpeza de nome de arquivo
        safe_title = "".join([c for c in doc_title if c.isalpha() or c.isdigit() or c in (' ', '-', '_')]).rstrip()
        safe_title = safe_title.replace("/", "-")
        
        print(f"⬇️  Baixando: {safe_title}...")
        
        try:
            # documents.info para pegar o Markdown
            payload_info = {"id": doc_id}
            res_info = requests.post(f"{BASE_URL}/documents.info", json=payload_info, headers=headers)
            
            if res_info.status_code == 200:
                conteudo_md = res_info.json().get('data', {}).get('text', '')
                
                filename = os.path.join(output_dir, f"{safe_title}.md")
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(f"# {doc_title}\n\n")
                    f.write(conteudo_md)
                print(f"   ✓ Salvo")
                sucessos += 1
            else:
                print(f"   ❌ Erro {res_info.status_code}: {res_info.text}")
                erros += 1
                
        except Exception as e:
            print(f"   ❌ Erro de exceção: {e}")
            erros += 1

    print("\n" + "="*30)
    print(f"🏁 Extração Concluída!")
    print(f"Arquivos salvos em: {os.path.abspath(output_dir)}")
    print(f"Sucessos: {sucessos} / {len(children)}")
    print("="*30)

if __name__ == "__main__":
    extrair_daia()
