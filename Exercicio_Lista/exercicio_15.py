nome = input("Digite o nome: ")
nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

nf = float(input("Digite o numero de faltas: "))
notaresult = (nota1+nota2+nota3)/3
faltas = 0,25 * nf
if (notaresult >= 7 and faltas >= 60):
    print("Aprovado")
elif (notaresult <= 6 and faltas >= 60):
    print("Reprovado na media")
elif (notaresult >= 7 and faltas <= 60):
    print("Reprovado em falta")
