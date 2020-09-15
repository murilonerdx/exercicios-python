p = float(input("Digite o valor do produto: "))

lucro = 0.45 * p
lucro2 = 0.3 * p

if (p < 20):
    lucro = 0.45 * p
    print("O valor de venda para o produto é ", p - lucro)
else:
    lucro = 0.3 * p
    print("O valor de venda para o produto é ", p - lucro)
