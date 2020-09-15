a = int(input("Digite o labo a do Triangulo: "))
b = int(input("Digite o labo b do Triangulo: "))
c = int(input("Digite o labo c do Triangulo: "))


if (a == b and b==c):
    print("O triangulo é equilatero")

elif (a != b and b==c or a==b and b != c ):
    print("O triangulo é isoceles")

else:
    print("Triangulo escaleno")
