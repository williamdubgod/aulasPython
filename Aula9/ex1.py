# Criando um dicionário vazio para armazenar os clientes
clientes = {}

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

    # Cria um dicionário com as informações do cliente (incluindo a conta bancária, se houver)
    cliente = {
        "email": email,
        "idade": idade,
        "conta_bancaria": conta_bancaria
    }

    # Adiciona o dicionário à variável clientes, utilizando o nome como chave
    clientes[nome] = cliente

    # Adiciona a conta bancária ao set de contas bancárias do cliente (se houver)
    if len(conta_bancaria) > 0:
        clientes[nome]['conta_bancaria'].add(conta)

# Exibe todos os clientes e suas respectivas contas bancárias (se houver)
for nome, cliente in clientes.items():
    print(f"Nome: {nome}")
    print(f"Email: {cliente['email']}")
    print(f"Idade: {cliente['idade']}")
    if len(cliente['conta_bancaria']) > 0:
        for conta in cliente['conta_bancaria']:
            print("Conta bancária:")
            print(f"Agência: {conta[0]}")
            print(f"Número: {conta[1]}")
            print(f"Saldo: {conta[2]}")
    else:
        print("O cliente não tem conta bancária")
    print("="*30)
