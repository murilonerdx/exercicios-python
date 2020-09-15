num = 1
b = 0

senhaGeral = 'yN1825*a'  
passValue = ''

# Criando as listas
lista_CodigoProduto = []
lista_DescricaoProduto = []
lista_QuantidadeProduto = []


def validacaoSenha(senha):
    tentativas = 0
    global passValue
    passValue = 'yN1825*a'
    if senha != senhaGeral and passValue != senhaGeral:
        while tentativas < 4:
            senha = input("Senha invalida, tente novamente: ")
            if senha == senhaGeral:
                tentativas = 4
            else:
                tentativas = tentativas + 1
                if tentativas == 3:
                    print("Voce errou muitas vezes, tente novamente mais tarde.")
                    sys.exit()


def cadastrarProduto():
    try:
        cdProduto = int(input("Digite o codigo do produto: "))

        if cdProduto in lista_CodigoProduto:
            print("Este codigo ja existe no sistema!")
        else:
            descProduto = input("Digite a descricao do produto até 20 carateres: ")
            if len(descProduto) > 20:
                print("ERRO, descrição excede o número de caracter.")
            else:
                quantProduto = int(input("Digite a quantidade em estoque do produto: "))
                if quantProduto <= 0:
                    print("Quantidade invalida")
                else:
                    lista_CodigoProduto.append(cdProduto)
                    lista_DescricaoProduto.append(descProduto)
                    lista_QuantidadeProduto.append(quantProduto)
                    print("Produto cadastrado com sucesso!")
    except:
        print("\033[31mERRO\033[0;0m Digite apenas números")


def alterarProduto():
    try:
        produtoAlterar = int(input("Digite o codigo do produto que deseja alterar: "))
        if produtoAlterar in lista_CodigoProduto:
            posicao = lista_CodigoProduto.index(produtoAlterar)
            print("Descricao: {}  Quantidade: {}".format(lista_DescricaoProduto[posicao], lista_QuantidadeProduto[posicao]))
            alterarDescricao = input("Digite a descricao do produto até 20 carateres: ")
            if len(alterarDescricao) > 20:
                print("ERRO, descrição excede o número de caracter.")
            lista_DescricaoProduto[posicao] = alterarDescricao
            alterarQuantidade = int(input("Qual a nova quantidade?: "))
            if alterarQuantidade <= 0:
                print("Quantidade invalida")
            else:
                lista_QuantidadeProduto[posicao] = alterarQuantidade
                print("Nova Descricao: {}  Nova Quantidade: {}".format(lista_DescricaoProduto[posicao],
                                                                       lista_QuantidadeProduto[posicao]))
        else:
            print("Produto nao cadastrado.")
    except:
        print("Digite um número!")

def excluirProduto():
    try:
        produtoAlterar = int(input("Digite o codigo do produto que deseja excluir: "))
        if produtoAlterar in lista_CodigoProduto:
            posicao = lista_CodigoProduto.index(produtoAlterar)
            print("Descricao: {}  Quantidade: {}".format(lista_DescricaoProduto[posicao], lista_QuantidadeProduto[posicao]))
    
            confirmar = int(input("DESEJA EXCLUIR O PRODUTO? : [0] SIM / [1] NÃO: "))
            if confirmar == 0:
                lista_CodigoProduto.pop(posicao)
                lista_DescricaoProduto.pop(posicao)
                lista_QuantidadeProduto.pop(posicao)
                print("Produto excluido com sucesso!")
    
            else:
                print("PRODUTO NÃO EXCLUÍDO")
        else:
            print("Produto não encontrado.")
    except:
        print("Digite apenas números!")


def listarProduto():
        if len(lista_CodigoProduto) == 0:
            print("Nenhum item na lista")
        else:
            print("CÓDIGO DO PRODUTO        DESCRIÇÃO                QUANTIDADE")
            print("-----------------        -----------------        ------------------")
            soma = 0
            for x in range(len(lista_CodigoProduto)):
                soma = sum(lista_QuantidadeProduto)
                qtdItem = len(lista_CodigoProduto)
                print("{:<24} {:<24} {:>0}".format(lista_CodigoProduto[x], lista_DescricaoProduto[x],
                                                   lista_QuantidadeProduto[x]))
            print("Quantidade de produto no estoque: {} ".format(soma))
            print("Total de produtos cadastrados: {}".center(20).format(qtdItem))
            somaMinima = 0
            for y in lista_QuantidadeProduto:
                if y < 100:
                    somaMinima += 1
            print("Produtos com estoque abaixo do minimo permitido(100): {}".format(somaMinima))
        
def comprarProduto():
    try:
        produtoAlterar = int(input("Digite o código do produto que deseja comprar: "))
        if produtoAlterar in lista_CodigoProduto:
            posicao = lista_CodigoProduto.index(produtoAlterar)
            print("Descrição: {}  Quantidade: {}".format(lista_DescricaoProduto[posicao], lista_QuantidadeProduto[posicao]))
            valor = int(lista_QuantidadeProduto[posicao])
            comprar = int(input("Quantidade que deseja comprar: "))
            if comprar <= 0:
                print("ERROR NENHUM PRODUTO COMPRADO")
            else:
                lista_QuantidadeProduto[posicao] = valor + comprar
                print("Nova Descrição: {}  Nova Quantidade: {}".format(lista_DescricaoProduto[posicao],
                                                                       lista_QuantidadeProduto[posicao]))
    
        else:
            print("PRODUTO NAO CADASTRADO")
    except:
        print("Digite apenas números!")


def venderProduto():
    try:
        produtoAlterar = int(input("Digite o código do produto que deseja vender: "))
        if produtoAlterar in lista_CodigoProduto:
            posicao = lista_CodigoProduto.index(produtoAlterar)
            print("Descrição: {}  Quantidade: {}".format(lista_DescricaoProduto[posicao], lista_QuantidadeProduto[posicao]))
    
            valor = int(lista_QuantidadeProduto[posicao])
            vender = int(input("Quantidade que deseja vender: "))
            if vender <= 0:
                print("ERROR NENHUM PRODUTO VENDIDO")
            else:
                if vender < valor:
                    lista_QuantidadeProduto[posicao] = valor - vender
                    print("Nova Descrição: {}  Nova Quantidade: {}".format(lista_DescricaoProduto[posicao],
                                                                           lista_QuantidadeProduto[posicao]))
                else:
                    print("Venda não permitida, quantidade maior que a de estoque.")
        else:
            print("PRODUTO NAO CADASTRADO")
    except:
        print("Digite apenas números!")



while num == 1 or num <= 6:
    # Criando o menu
    print("|##[-Menu de Opcoes-]##|")
    print("1. Cadastrar Produto")
    print("2. Alterar produto")
    print("3. Excluir produto")
    print("4. Listar estoque de produtos")
    print("5. Comprar produto")
    print("6. Vender produto")
    print("7. Sair")

    num = int(input("Digite o número da opção desejada: "))
    while num > 7 or num < 1:
        num = int(input("Opcao desejada invalida, digite novamente: "))

    # Primeira opcao do menu - CADASTRAR PRODUTO
    if num == 1:
        cadastrarProduto()

    # Segunda opção do menu - ALTERAR PRODUTO
    if num == 2:
        if len(lista_CodigoProduto) == 0:
            print("PRODUTO NAO CADASTRADO")
        else:
            if passValue == senhaGeral:
                alterarProduto()
            else:
                senha = input("Digite a senha para acessar o sistema: ")
                validacaoSenha(senha)
                alterarProduto()

    # Terceira opï¿½ï¿½o do menu - EXCLUIR PRODUTO
    if num == 3:

        if len(lista_CodigoProduto) == 0:
            print("PRODUTO NAO CADASTRADO")
        else:
            if passValue == senhaGeral:
                excluirProduto()
            else:
                senha = input("Digite a senha para acessar o sistema: ")
                validacaoSenha(senha)
                excluirProduto()

    # Quarta opção do menu - LISTAR PRODUTOS
    if num == 4:
        listarProduto()

    # Terceira do menu - COMPRAR PRODUTO
    if num == 5:
        if len(lista_CodigoProduto) == 0:
            print("PRODUTO NAO CADASTRADO")
        else:
            comprarProduto()

    if num == 6:  # VENDER PRODUTO
        if len(lista_CodigoProduto) == 0:
            print("PRODUTO NAO CADASTRADO")
        else:
            venderProduto()

# Ultima opção do menu - SAIR DO PROGRAMA
else:
    print("Saindo...")
