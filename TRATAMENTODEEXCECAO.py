#tratamento de exceção

try: #tenta fazer algo
    x = int(input('Digite sua idade: '))
except: #executa quando o try dá errado.
    print('Certifíque-se de que digitou somente números.')
else: #executa quando o try dá certo
    print(f'Sua idade é {x}')
finally: #executa apesar de qualquer coisa
    print('Registrado com sucesso !')