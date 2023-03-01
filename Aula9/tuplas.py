#As Tuplas são imutáveis, logo não permitem os metodos das listas.

lista = ["São Paulo", "Rio de Janeiro", 105]

tupla = ("São Paulo", "Rio de Janeiro", 105)

lista.append("Bahia")

print(lista)

print("Rio de Janeiro" in tupla) # O operador in verifica se existe aquela propriedade na tupla
print(105 in tupla)
print("Espírito Santo" in tupla)


print(tupla.count("São Paulo"))
print(tupla.count("Espírito Santo"))


tupla_nomes = ('Maria', 'João', 'Paulo', 'Pedro', 'Maria', 'Sérgio')


print(tupla_nomes.index('Maria'))


# Pesquisa a partir do segundo elemento até o quinto elemento (opcional)
print(tupla_nomes.index('Maria', 2, 5))

sexo = ("M", "m", "F", "f")

digite = input("Digite o sexo: ")

while (digite not in sexo):
    print("Sexo inválido")
    break