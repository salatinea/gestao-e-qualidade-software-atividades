import requests

def buscar_clima(cidade):
    
    url = f"https://api.exemplo/clima?cidade={cidade}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        dados = response.json()
    except requests.RequestException as e:
        raise ValueError(f"Erro na requisição: {e}")

    if "temperatura" not in dados:
        raise ValueError("Resposta inválida: 'temperatura' não encontrada.")

    return dados["temperatura"]
