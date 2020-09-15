num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))
num3 = float(input("Digite o terceiro valor: "))

if ((num1 > num2 and num2>=num3)):
    print("os valores em ordem decrescente é: ", num1, num2, num3)

elif (num1 > num3 and num3 >= num2):
    print("os valores em ordem decrescente é: ", num1, num3, num2)
    
elif (num2 > num1 and num1 >= num3):
    print("os valores em ordem decrescente é: ", num2, num1, num3)

elif (num2 > num3 and num3 >=num1):
    print("os valores em ordem decrescente é: ", num2, num3, num1)

elif (num3 > num2 and num2 >= num1):
    print("os valores em ordem decrescente é: ", num3, num2, num1)

elif (num3 > num1 and num1 >= num2):
    print("os valores em ordem decrescente é: ", num3, num1, num2)
