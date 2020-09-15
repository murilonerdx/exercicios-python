# -*- coding: cp1252 -*-
code = {}
info = []
lista_produtos = {}
cd = []
ds = []
qt = []
acesso = []
n = 1
geral = []

while (n != 7):

    print("============================")
    print("#-------[MENU LISTA]-------#")
    print("1 - Cadastrar produto")
    print("2 - Alterar produto")
    print("3 - Excluir produto")
    print("4 - Listar estoque de peças")
    print("5 - Comprar produto")
    print("6 - Vender produto")
    print("7 - Sair")
    print("=======[@by Murilo@]=======")
    print("=============================")

    


        
    def validacao(cd_produto):
        for x in lista_produtos['codigo']:
            if x == cd_produto:
                print("###[-CODIGO JA EXISTENTE-]###")
            else:
                print("=============")
                listando()
              
         





    def alterar():
        codigo_produto = raw_input("Digito o codigo do produto a ser alterado: ")
        verifica(cd_produto)
        
        desejo = int(input("Deseja alterar ? [ 1 - SIM |#| 2 - NAO ]: "))
        if desejo == 1:
            nova_ds = raw_input("Digite a nova descricao: ")
            nova_qt = raw_input("Digite o novo estoque: ")
            lista_produtos['descricao'].remove(lista_produtos['descricao'][0])
            lista_produtos['quantidade'].remove(lista_produtos['quantidade'][0])
            lista_produtos['descricao'].insert(0, nova_ds)
            lista_produtos['quantidade'].insert(0, nova_qt)
            print("##########[-ATUALIZADO-]##########")
            print('Descrição: {0} | ESTOQUE: {1}'.format(lista_produtos['descricao'], lista_produtos['quantidade']))
        elif desejo == 2:
            print("RETORNANDO")
            
        else:
            print("OPCAO NAO EXISTE")
    
    def verifica():
        for x in lista_produtos['codigo']:
            if x == cd_produto:
                for codigo_produto in lista_produtos['codigo']:
                    print('Descrição: {0} | ESTOQUE: {1}'.format(lista_produtos['descricao'], lista_produtos['quantidade']))
            else:
                print("PRODUTO NÃO CADASTRADO")
    def getCode():
                    
            codigo = lista_produtos['codigo']
            descricao = lista_produtos['descricao']
            quantidade = lista_produtos['quantidade']
            codigoAcesso = lista_produtos['acesso']
        
        
        
        
        
            geral.append(codigo)
            geral.append(descricao)
            geral.append(quantidade)
            geral.append(codigoAcesso)

            code['CODIGO'] = codigo
            info.append(codigo)

            
        
        
    def listando():
        cd_produto = raw_input("Digite o codigo do produto: ")
        
        lista_produtos['codigo'] = cd
        cd.append(cd_produto)
            
        ds_produto = raw_input("Digite a descrição do produto: ")
            
        lista_produtos['descricao'] = ds
        ds.append(ds_produto)
            
        qt_produto = raw_input("Digite a quantidade de produto: ")
            
        lista_produtos['quantidade'] = qt
        qt.append(qt_produto)
            
        senha_produto = raw_input("Digite sua senha de acesso: ")
            
        lista_produtos['acesso'] = acesso
        acesso.append(senha_produto)
                
        
        continuar()
        
        
            
    def adicionarLista():  
        if len(lista_produtos) <= 0:
            listando()    
        elif len(lista_produtos) > 0:
            cd_produto = raw_input("Digite o codigo do produto  PARA VERIFICAR: ")
            validacao(cd_produto)
            
            
        else:
            listando()
            
    def continuar():
            verbose_add = 0
            while (verbose_add == 0):
                adicionarMais = int(input("Deseja adicionar mais na lista ? | 1 - SIM: 2 - NÃO | : "))
                
                if adicionarMais == 1:
                    verbose = 0
                    
                    cd_produto = raw_input("Digite o codigo do produto: ")
                    validacao(cd_produto)
                    
                elif adicionarMais == 2:
                    print("Retornando")
                    verbose_add = 1
                    
                    
                else:
                    print("Numero não existe")
                    verbose_add = verbose_add + 1    
            
    opcao = int(input("Digite a opcao desejada: "))

    if 0<opcao<7:
        if opcao == 1:
            adicionarLista()
            
        if opcao == 2:
            if len(lista_produtos) <= 0:
                print("#######################")
                print("Nenhuma item cadastrado")
                print("#######################")
            elif len(lista_produtos) > 0:
        
                a = 0
                while a < 3:
                    if lista_produtos == None:
                        print("O ESTOQUE ESTÁ VAZIO")
                        a = 3
                    else:
                        senha = raw_input("Senha de acesso para alteração: ")
                        if senha == 'yN1825*a':
                            print("####[-SENHA CORRETA-]####")
                            
                            alterar()
                            a = 3
                        
                        elif senha != 'yN1825*a':
                            print("####[-SENHA INCORRETA-]####")
                    
                

                    
    elif opcao == 7:
        print("####[-SAINDO-]####")
        n = 7
    else:
        print("####[-OPCAO INVALIDA-]####")   
            
            
