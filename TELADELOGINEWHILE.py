#tela_de_login + treino de while

while True:
    num = int(input('Digite:\n1- Logar\n2- Cadastro\n3- Sair\n'))
    if num == 1:
        login = input('Digite seu loging:')
        senha = int(input('Digite sua senha:'))
        print('Seja bem vindo :D')

    elif num == 2:
        nome = input('Digite o seu nome: ')
        nome = nome.title()
        cpf = int(input('Digite o seu cpf: '))
        datnasc = input('Digite sua data de nascimento:')
        sexo = input('Qual o seu sexo: M/F: ')
        sexo = sexo.lower()
        print(f'Nome:{nome} / CPF:{cpf}\nNascimento:{datnasc} / Sexo:{sexo} / ')
        confirm = input('Deseja confirmar ? S/N')
        confirm = confirm.lower()
        if confirm == 's':
            print('Seus dados foram cadastrados !')
        else:
            print('Voltando para tela inicial ...')

    elif num == 3:
        break

    else:
        print('Número inválido !')


print('Você saiu da tela.')



x = -1

while x < 11:
    if x == 5:
        continue

    print(x)
    x+=1







