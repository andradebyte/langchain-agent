import json
import requests

# Configurações da API
API_URL = "http://localhost:8000/api/v1/weaviate/index"

def load_projects(file_path):
    """Carrega os projetos do arquivo JSON"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            print(f"✓ {len(data)} projetos carregados com sucesso")
            return data
    except FileNotFoundError:
        print(f"✗ Erro: Arquivo '{file_path}' não encontrado")
        return None
    except json.JSONDecodeError as e:
        print(f"✗ Erro ao decodificar JSON: {e}")
        return None

def post_project(project):
    """Envia um projeto individual para a API"""

    payload = {
        "title": project["title"],
        "description": project["description"],
        "tags": project["tags"]
    }
    
    try:
        response = requests.post(
            API_URL,
            json=payload,
            headers={"Content-Type": "application/json"}
        )
        
        if response.ok:
            print(f"✓ '{project['title']}' indexado com sucesso (Status: {response.status_code})")
            return True
        else:
            print(f"✗ Erro ao indexar '{project['title']}': {response.status_code}")
            print(f"  Resposta: {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"✗ Erro de conexão ao indexar '{project['title']}': {e}")
        return False

def main():
    """Função principal"""
    # Carrega os projetos
    projects = load_projects('../../data/projetos.json')
    
    if not projects:
        return
    
    # Estatísticas
    success_count = 0
    failed_count = 0
    
    print(f"\n{'='*60}")
    print(f"Iniciando indexação de {len(projects)} projetos...")
    print(f"{'='*60}\n")
    
    # Envia cada projeto
    for idx, project in enumerate(projects, 1):
        print(f"[{idx}/{len(projects)}] ", end="")
        
        if post_project(project):
            success_count += 1
        else:
            failed_count += 1
    
    # Resumo final
    print(f"\n{'='*60}")
    print(f"Indexação concluída!")
    print(f"  ✓ Sucesso: {success_count}")
    print(f"  ✗ Falhas: {failed_count}")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
