# Criando uma lista vazia para armazenar os clientes
clientes = []

# Loop para cadastrar os clientes
while True:
    # Solicita as informações do cliente
    nome = input("Digite o nome do cliente (ou digite 'sair' para finalizar): ")
    if nome.lower() == "sair":
        break

    email = input("Digite o email do cliente: ")
    idade = int(input("Digite a idade do cliente: "))

    # Cria um set vazio para armazenar os dados da conta bancária (se houver)
    conta_bancaria = set()

    # Pergunta se o cliente tem conta bancária
    resposta = input("O cliente tem conta bancária? (s/n): ")

    if resposta.lower() == "s":
        # Solicita os dados da conta bancária
        agencia = input("Digite a agência da conta bancária: ")
        numero = input("Digite o número da conta bancária: ")
        saldo = float(input("Digite o saldo da conta bancária: "))

        # Cria uma tupla com os dados da conta bancária
        conta = (agencia, numero, saldo)

        # Adiciona a tupla à variável conta_bancaria
        conta_bancaria.add(conta)

    # Cria uma tupla com as informações do cliente (incluindo a conta bancária, se houver)
    cliente = (nome, email, idade, conta_bancaria)

    # Adiciona a tupla à lista clientes
    clientes.append(cliente)

# Exibe todos os clientes e suas respectivas contas bancárias (se houver)
for cliente in clientes:
    nome, email, idade, conta_bancaria = cliente
    print(f"Nome: {nome}")
    print(f"Email: {email}")
    print(f"Idade: {idade}")
    if len(conta_bancaria) > 0:
        for conta in conta_bancaria:
            print("Conta bancária:")
            print(f"Agência: {conta[0]}")
            print(f"Número: {conta[1]}")
            print(f"Saldo: {conta[2]}")
    else:
        print("O cliente não tem conta bancária")
    print("="*30)
