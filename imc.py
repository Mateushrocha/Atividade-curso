"""peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))
"""
peso = 73
altura = 175

imc = peso / (altura * altura)

print(int(imc))

if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 24.9:
    print("Peso normal")
elif 25 <= imc < 29.9:
    print("Sobrepeso")
else:
    print("Obesidade")

