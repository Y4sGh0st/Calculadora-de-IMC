peso = float(input("Digite seu peso: ").replace(",", "."))
altura = float(input("Digite sua altura: ").replace(",", "."))

imc = peso / (altura ** 2)

print("Seu IMC é:", round(imc, 2))

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso normal")
elif imc < 30:
    print("Sobrepeso")
else:
    print("Obesidade")
    