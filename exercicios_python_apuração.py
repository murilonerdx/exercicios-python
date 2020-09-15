print("Candidatos: | Roberto, Davi, e João |")
roberto = int(input("Quantos votos Roberto recebeu ?: "))
davi = int(input("Quantos votos Davi recebeu ?: "))
joao = int(input("Quantos votos Joao recebeu ?: "))
votos_nulos = int(input("Quantos votos foram nulos ?: "))
votos_brancos = int(input("Quantos votos em branco ?: "))
numeleitores = (davi+joao+roberto+votos_nulos+votos_brancos)
porcentualtotal = ((davi+joao+roberto)*100)/(numeleitores)
print("Porcentual valido é :",round(porcentualtotal),"%")
robertop = roberto/numeleitores
davip = davi/numeleitores
joaop = joao/numeleitores
num = votos_nulos+votos_brancos
porcentualbranco = num/numeleitores
votosb = votos_brancos/numeleitores
votosn = votos_nulos/numeleitores
print("Numero de eleitores é de: ",numeleitores)
print("Porcentual de todos dos candidatos")
print("Porcentual do Roberto: ", (round(robertop, 2))*100,"%")
print("Porcentual do Davi: ", (round(davip, 2))*100,"%")
print("Porcentual do Joao: ", (round(joaop, 2))*100,"%")
print("Porcentual de votos brancos e nulos: [", (round(porcentualbranco, 2))*100,"]%")
print("Porcentual de votos brancos: [",(round(votosb, 2))*100,"]%")
print("Porcentual de votos nulos: [",(round(votosn, 2))*100,"]%")
print(" ___________NUMERO CANDIDATOS : [",numeleitores,"]_____________________")
print("[ROBERTO]_______________[DAVI]_______________[JOAO]")
print("[",roberto,"]__________________[",davi,"]_________________[",joao,"]")
print("[",round(robertop*100),"%]__________________[",round(davip*100),"%]_______________[",round(joaop*100),"%]")
