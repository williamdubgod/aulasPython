alunosVestibular = 'Jose dos Santos,7,Sao Paulo;Sandra Silva,6.5,Sao Jose do Rio Preto;Augusto Soares,8,Sao Paulo;Vanderlei Azevedo,5.65,Santos;Vanessa Ferreira,9,Sao Paulo;Natan Cruz,10,Sao Paulo.'
alunosList = alunosVestibular.split(';')
alunosAprovados = {}
for aluno in alunosList:
    alunoInfo = aluno.split(',')
    nome = alunoInfo[0]
    nota = float(alunoInfo[1])
    cidade = alunoInfo[2]
    if nota >= 7:
        alunosAprovados[nome] = {'Nota': nota, 'Cidade': cidade}

for nome, info in alunosAprovados.items():
    print(f'Nome: {nome}\nNota: {info["Nota"]}\nCidade: {info["Cidade"]}\n')