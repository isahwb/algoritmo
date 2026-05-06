#Calcule média de duas notas e informe situação aprovado >=7, recuperação>=5, reprovado.

nota1 = float(input("Digite a primeira nota: "))

if nota1>=7:
    print("Aprovado")
elif nota1>=5:
    print("Recuperação")
else:
    print("Reprovado")