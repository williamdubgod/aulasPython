#API domínio web

import requests

dominio = input("Digite o domínio desejado: ")
url = f"https://brasilapi.com.br/api/registrobr/v1/{dominio}.com.br"

response = requests.get(url)

if response.status_code == 200:
    dados = response.json()
    if({dados['status']} == {'AVAILABLE'}):
        print("Domínio disponível!")

if({dados['status']} != {'AVAILABLE'}):
    print("Domínio já utilizado!")
    print("Expira em: " + dados['expires-at'])