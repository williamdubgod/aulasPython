#API GitHub

import requests

usuario = input("Digite seu usário do GitHub: ")
url = f"https://api.github.com/users/{usuario}"

response = requests.get(url)

if response.status_code == 200:
    dados = response.json()
    print(f"Nome: {dados['name']}")
    print(f"Quantidade de repositórios: {dados['public_repos']}")
    print(f"Seguidores: {dados['followers']}")
else:
    print("Usuário não encontrado.")