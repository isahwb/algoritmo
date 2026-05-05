# verifique se um número é positivo, negativo ou zero


numr= int (input("Digite um numero:"))
if numr > 0:
     print(f'O número {numr} é positvo')
elif numr < 0:
     print(f'O número {numr} é negativo')
else:
     print(f'O número {numr} é zero')