#API Moedas

import requests

valor = float(input("Insira um valor que gostaria de converter: "))
converter = input("Em que moeda você gostaria de converter o real Dolar(D), Euro(E) ou BitCoin(B)? ").upper()

if converter == 'D':
    url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'
    response = requests.get(url)

elif converter == 'E':
    url = 'https://economia.awesomeapi.com.br/json/last/EUR-BRL'
    response = requests.get(url)

else:
    url = 'https://economia.awesomeapi.com.br/json/last/BTC-BRL'
    response = requests.get(url)

if response.status_code == 200:
    dados = response.json()
    if converter == "D":
        total = float(dados['USDBRL']['ask'])
    elif converter == "E":
        total = float(dados['EURBRL']['ask'])
    else:
        total = float(dados['BTCBRL']['ask'])

    print(f'{valor/total:.2f}')
    
else:
    print("Moeda não encontrada.")