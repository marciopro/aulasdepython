nome = input('Digite seu nome: ')
nome = nome.title()
idade = int(input('Digite sua idade: '))
nota1 = float(input('Digite a nota da prova 1: '))
nota2 = float(input('Digite a nota da prova 2: '))
media = (nota1+nota2)/2

if media>=6.0 and idade>=18:

    print(f'{nome} está aprovado')
else:
    print(f'{nome} está reprovado')



