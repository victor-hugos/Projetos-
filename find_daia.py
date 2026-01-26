import requests
import json

API_KEY = "ol_api_8SNMXz3Qgx4AuuT8tlkUEymeXJ7dJATBeQ8Vbc"
BASE_URL = "https://portal.zello.space/api"
SEARCH_TERM = "DAIA"
SEARCH_ID_FRAGMENT = "rqvv1YzyHd"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

def find_daia():
    print("🚀 Iniciando varredura em todas as coleções...")
    
    # 1. Pegar todas as coleções
    try:
        res = requests.post(f"{BASE_URL}/collections.list", headers=headers, json={})
        if res.status_code != 200:
            print("❌ Falha ao listar coleções.")
            return
        collections = res.json().get('data', [])
    except Exception as e:
        print(f"Erro fatal: {e}")
        return

    found_docs = []

    # Função recursiva para buscar na árvore
    def search_tree(nodes, collection_name):
        for node in nodes:
            title = node.get('title', 'Sem título')
            doc_id = node.get('id')
            url_id = node.get('urlId', '')
            
            # Checar se bate com o termo ou ID
            match_title = SEARCH_TERM.lower() in title.lower()
            match_id = SEARCH_ID_FRAGMENT in doc_id or SEARCH_ID_FRAGMENT in url_id
            
            if match_title or match_id:
                found_docs.append({
                    "title": title,
                    "id": doc_id,
                    "urlId": url_id,
                    "collection": collection_name,
                    "children_count": len(node.get('children', []))
                })
            
            # Busca recursiva nos filhos
            if 'children' in node and node['children']:
                search_tree(node['children'], collection_name)

    # 2. Iterar sobre cada coleção
    for col in collections:
        col_name = col['name']
        col_id = col['id']
        print(f"📂 Verificando: {col_name}...")
        
        try:
            res_tree = requests.post(f"{BASE_URL}/collections.documents", headers=headers, json={"id": col_id})
            if res_tree.status_code == 200:
                tree_data = res_tree.json().get('data', [])
                search_tree(tree_data, col_name)
        except Exception as e:
            print(f"   Erro ao ler coleção: {e}")

    # 3. Resultado
    print("\n" + "="*40)
    if found_docs:
        print(f"✅ ENCONTRADOS {len(found_docs)} DOCUMENTOS:")
        for doc in found_docs:
            print(f"📄 Título: {doc['title']}")
            print(f"   ID: {doc['id']}")
            print(f"   URL ID: {doc['urlId']}")
            print(f"   Coleção: {doc['collection']}")
            print(f"   Filhos: {doc['children_count']}")
            print("-" * 20)
    else:
        print("❌ Nenhum documento encontrado com 'DAIA' ou o ID fornecido.")
    print("="*40)

if __name__ == "__main__":
    find_daia()
