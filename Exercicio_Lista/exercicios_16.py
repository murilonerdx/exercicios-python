print("Um número digitado está compreendido entre 0 e 30 ou entre 40 e 79 ou fora dos limites estabelecidos")
num1 = int(input("Digite o primeiro valor: "))

if (num1 <= 30 and num1 >=0):
    print("Numero compreendido entre 0 e 30")
elif ( num1 <=79 and num1 >=40):
    print("Fora dos limites estabelecidos")
