import requests
import json

API_KEY = "ol_api_8SNMXz3Qgx4AuuT8tlkUEymeXJ7dJATBeQ8Vbc"
BASE_URL = "https://portal.zello.space/api"
TARGET_ID = "rqvv1YzyHd"
TEST_COLLECTION_ID = "744fb106-1ca7-4c1a-ba3a-ed0a939f48c2" # Diretoria Comercial

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

def deep_probe():
    print(f"🕵️‍♂️ Investigação Profunda para ID: {TARGET_ID}")

    # 1. Tentar documents.info com shareId
    print("\n--- 1. Tentar documents.info usando shareId ---")
    try:
        res = requests.post(f"{BASE_URL}/documents.info", headers=headers, json={"shareId": TARGET_ID})
        if res.status_code == 200:
            doc = res.json().get('data', {})
            print(f"✅ SUCESSO! Encontrado via shareId.")
            print(f"   Título: {doc['title']}")
            print(f"   ID Real (UUID): {doc['id']}")
            print(f"   Collection ID: {doc['collectionId']}")
            return # Se achou, paramos por aqui!
        else:
            print(f"❌ shareId falhou: {res.status_code}")
    except Exception as e:
        print(f"Erro: {e}")

    # 2. Tentar listar documentos de uma coleção conhecida (Teste de permissão)
    print(f"\n--- 2. Teste de Permissão: Listar docs da coleção {TEST_COLLECTION_ID} ---")
    try:
        # Tentar collections.documents (estrutura de árvore)
        res = requests.post(f"{BASE_URL}/collections.documents", headers=headers, json={"id": TEST_COLLECTION_ID})
        if res.status_code == 200:
            print("✅ collections.documents funcionou para a coleção de teste!")
            data = res.json()
            # print(json.dumps(data, indent=2)[:500])
        else:
            print(f"❌ collections.documents falhou: {res.status_code}")
            
            # Tentar documents.list
            print("   Tentando documents.list...")
            res2 = requests.post(f"{BASE_URL}/documents.list", headers=headers, json={"collectionId": TEST_COLLECTION_ID})
            if res2.status_code == 200:
                 print("✅ documents.list funcionou para a coleção de teste!")
            else:
                 print(f"❌ documents.list falhou também: {res2.status_code}")

    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    deep_probe()
