salario = int(input("Digite o valor do salario: "))
prestacao = int(input("Digite o valor da prestação: "))
sp = int(salario*0.3 + salario)
if (int(prestacao >= sp)):
    print("o valor da prestacao é maior: ")
else:
    print("Prestação Aceita")
