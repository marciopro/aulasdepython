import pymysql.cursors

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='erp',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

autentico = False

def logarCadastrar():
    usuarioExistente = 0
    autenticado = False
    usuarioMaster = False

    if decisao == 1:
        nome = input('Digite seu nome: ')
        senha = input('Digite sua senha: ')

        for linha in resultado:
            if nome == linha['nome'] and senha == linha['senha']:
                if linha['nivel'] == 1:
                    usuarioMaster = False
                elif linha['nivel'] == 2:
                    usuarioMaster = True
                autenticado = True
                print('autenticado !')
                break
            else:
                autenticado = False

        if not autenticado:
            print('email ou senha incorretos')

    elif decisao == 2:
        print('Faça seu cadastro')
        nome = input('Digite seu nome: ')
        senha = input('Digite sua senha: ')

        for linha in resultado:
            if nome == linha['nome'] and senha == linha['senha']:
                usuarioExistente = 1
        if usuarioExistente == 1:
            print('Usuario já cadastrado. Tente um nome ou senha diferentes.')
        elif usuarioExistente == 0:
            try:
                with conexao.cursor() as cursor:
                    cursor.execute('insert into cadastros(nome, senha, nivel) values("{}", "{}", "{}");'.format(nome, senha, 1))
                    conexao.commit()
                    print('Usuário cadastrado com sucesso !!!')
            except:
                print('Erro ao inserir os dados no banco.')

    return autenticado, usuarioMaster

def cadastrarProduto():
    nome = input('Digite o nome do produto: ')
    ingredientes = input('Digite os ingredientes do produto: ')
    grupo = input('Digite o grupo pertencente a este produto: ')
    preço = float(input('Digite o preço do produto: '))
    try:
        with conexao.cursor() as cursor:
            cursor.execute('insert into produtos (nome, ingredientes, grupo, preco) values (%s, %s, %s, %s);', (nome.title(), ingredientes.title(), grupo.title(), preço))
            conexao.commit()
            print('Produto cadastrado com sucesso !!!')
    except:
        print('Não foi possível inserir informações ao banco de dados.')

def listarProdutos():
    produtos = list()
    try:

        with conexao.cursor() as cursor:
            cursor.execute('select * from produtos')
            mostrarprodutos = cursor.fetchall()

    except:
        print('Erro ao tentar listar produtos')

    for i in mostrarprodutos:
        produtos.append(i)

    if len(produtos) != 0:
        for y in range(0, len(produtos)):
            print(produtos[y])
    else:
        print('Não há produtos cadastrados.')

def excluirProdutos():
    idDelete = int(input('Digite o ID do produto a ser excluído: '))
    try:
        with conexao.cursor() as cursor:
            cursor.execute('delete from produtos where id = {}'.format(idDelete))
            conexao.commit()
    except:
        print('Erro ao deletar produto do banco de dados.')

    print('Produto excluído com sucesso !!!')

def listarPedidos():
    armazenaPedidos = list()
    decides = False
    while not decides:
        armazenaPedidos.clear()

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from pedidos')
                pedidosList = cursor.fetchall()
        except:
            print('Não foi possível coletar os pedidos')

        for i in pedidosList:
            armazenaPedidos.append(i)

        if len(armazenaPedidos) != 0:
            for y in range(0, len(armazenaPedidos)):
                print(armazenaPedidos[y])
        else:
            print('Não há pedidos. !')

        try:
            apagadecisao = int(input('1 - APAGAR PEDIDO\n2 - VOLTAR PARA A LISTA\n0 - VOLTAR PARA O MENU INICIAL '))

            if apagadecisao == 1:
                idDelete = input('Digite o ID do pedido que deseja apagar: ')
                with conexao.cursor() as cursor:
                    cursor.execute('delete from pedidos where id ={}'.format(idDelete))
                    conexao.commit()
                    print('Pedido apagado com sucesso !!!')
            elif apagadecisao == 2:
                print('Voltando para lista de pedidos ...')
            elif apagadecisao == 0:
                print('Voltando para tela de MENU ...')
                decides = True

        except:
            print('Dígito inválido. Tente novamente')



while not autentico:
    decisao = int(input('1 - logar\n2 - cadastrar\n '))

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from cadastros')
            resultado = cursor.fetchall()

    except:
            print('Erro ao conectar no banco de dados.')

    autentico, usuarioSupremo = logarCadastrar()

if autentico:
    if usuarioSupremo == True:
        decisaoUsuario = 1
        while decisaoUsuario != 0:
            try:
                decisaoUsuario = int(input('0 - sair\n1 - cadastrar produto\n2 - listar produto\n3 - listar pedido\n'))

                if decisaoUsuario == 1:
                    cadastrarProduto()
                elif decisaoUsuario == 2:
                    listarProdutos()
                    deleteproduto = int(input('Deseja deletar algum produto ?\n1 - Sim\n0 - Não\n'))
                    if deleteproduto == 1:
                        excluirProdutos()
                    else:
                        print('Voltando a tela de menu... ')
                elif decisaoUsuario == 3:
                    listarPedidos()
                else:
                    print('Dígito inválido. Digite 0 para sair ou 1 para cadastrar.')
            except:
                print('Erro !! Tente novamente !')


