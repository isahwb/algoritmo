#Leia idade e classifique: criança, adulto ou idoso.

idade = int(input("Digite a idade: "))
if idade>=18 and idade<=60:
    print("Adulto")
elif idade>60:
    print("idoso")
else:
    print("Criança")