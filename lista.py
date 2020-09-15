# -*- coding: cp1252 -*-
n = 1
lista = []
while (n != 4):

    print("============================")
    print("#-------[MENU LISTA]-------#")
    print("1 - Adicionar na lista")
    print("2 - Remover da lista")
    print("3 - Ver lista")
    print("4 - Sair")
    print("=======[@by Murilo@]=======")
    print("=============================")

    
      

    
        
                
    def verificaLista():
        rmv = raw_input("Remover: ")
        for x in lista:
            lista.remove(rmv)
            

            
    def adicionarLista():
        
        
        dgtAdicionar = raw_input("Adicionar: ")
        lista.append(dgtAdicionar)

        verbose_add = 0
        while (verbose_add == 0):
            adicionarMais = int(input("Deseja adicionar mais na lista ? | 1 - SIM: 2 - NÃO | : "))
        
        
            if adicionarMais == 1:
                verbose = 0
                while (verbose == 0):
                    dgtAdicionar = raw_input("Adicionar: ")
                    lista.append(dgtAdicionar)
                    verbose = verbose + 1
                    
            elif adicionarMais == 2:
                print("Retornando")
                verbose_add = verbose_add + 1
                
            else:
                print("Numero não existe")
                verbose_add = verbose_add + 1
                
                
     
                
            
    
    opcao = int(input("Digite a opcao desejada: "))
    
    if 0<opcao<4:
        if opcao == 1:
            
            print("Digite um numero para adicionar: ")
            
            adicionarLista()
            
            

        elif opcao == 2:
            print("Remover da lista")
            print(lista)
            print("O que deseja remover ?")
            verificaLista()
            
           
        
        elif opcao == 3:
            
            print("=======[Essa é sua lista]========")
            
            print(lista)

    elif opcao == 4:
        print("Saindo")
        n = 4
    else:
        print("Opcao invalida")

    
            
            

