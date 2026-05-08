# Crie uma calculadora (+, -, *, /) usando escolha do usuário

n1 = float(input('Digite um número: '))
n2 = float(input('Digite mais um número: '))

print ('operações')
print ('1: adição')
print ('2: subtração')
print ('3: multiplicação')
print ('4: divisão')

operacao = input('escolha uma operação: ')

if operacao=='1':
    resultado1=(n1+n2)
    print (f'{n1} + {n2} = {resultado1}')
elif operacao=='2':
    resultado2=(n1-n2)
    print (f'{n1} - {n2} = {resultado2}')
elif operacao=='3':
    resultado3=(n1*n2)
    print (f'{n1} * {n2} = {resultado3}')
elif operacao =='4':
    resultado4=(n1/n2)
    print (f'{n1} / {n2} = {resultado4}')