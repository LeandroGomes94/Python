import aluno as al

qtd = int(input("Informe quantos alunos serão cadastrados: "))

for i in range(qtd):

    al.nome.append(input("Digite o nome do aluno: "))
    al.n1 .append(int(input("Digite a primeira nota: ")))
    al.n2.append(int(input("Digite a segunda nota: ")))
    al.media.append(al.calculaMedia(al.n1[i], al.n2[i]))
    al.resultado.append(al.verificaStatus(al.media[i]))


for i in range(qtd):

    print(al.nome[i])
    print(al.n1[i])
    print(al.n2[i])
    print(al.media[i])
    print(al.resultado[i])