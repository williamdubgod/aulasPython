def exibirMensagem():
    return 'Olá pessoal!'

print(exibirMensagem())

def calcularDivisao(a, b):
    v1 = float(a)
    v2 = float(b)

    result = v1 / v2

    return result

v1 = float(input("Digite o primeiro valor: "))
v2 = float(input("Digite o segundo valor: "))

print(f'A divisão de {v1} por {v2} é: {calcularDivisao(v1, v2)}')



