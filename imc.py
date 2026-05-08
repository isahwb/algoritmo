#Calcule IMC e classifique (baixo peso, normal, sobrepeso, obesidade)

peso=float(input('Digite seu peso (kg): '))
altura=float(input('Digite sua altura (m): '))

imc = peso / (altura**2)
print("Seu imc é: {:.2f}".format(imc))

if imc >= 25: 
    print("Você está acima do peso!")
elif imc >= 18.5: 
    print("Você está com peso normal!") 
else: 
    print("Você está abaixo do peso!")
    