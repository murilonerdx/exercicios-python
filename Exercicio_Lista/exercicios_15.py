nome = input("Digite seu nome: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

falta = int(input("Digite o numero de faltas: "))

media = (nota1+nota2+nota3)/3



if(media > 7.0 and 80 - falta > 60):
    print("Aprovado - [ ",nome," ]")
elif(media < 7.0 and 80 - falta <= 60):
    print("Reprovação por falta [ ",nome," ]")
elif(media < 7.0 and 80 - falta >= 60):
    print("Reprovação por media [ ",nome," ]")
