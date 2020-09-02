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


while not autentico:
    decisao = int(input('Digite 1 para logar ou 2 para cadastrar: '))

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from cadastros')
            resultado = cursor.fetchall()

    except:
            print('Erro ao conectar no banco de dados.')

    autentico, usuarioSupremo = logarCadastrar()
