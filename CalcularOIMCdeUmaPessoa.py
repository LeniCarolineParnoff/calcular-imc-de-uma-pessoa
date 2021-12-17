#Calcular o IMC de uma pessoa e imprimi-lo
#Regra de negocio:
#Para calcular IMC voce deve ler o peso e ler a altura e calcular de acordo com a formula
#Formula: peso/ (altura) ** 2 ("ao quadrado")


peso = float (input("Qual é o seu peso: "))
print('Seu peso é: ' + str (peso))
altura = float (input("Qual a sua altura: "))
print("Sua altura é: " + str (altura))
imc = peso/ (altura **2)

print('Seu IMC é: ' + str (imc))

if 24 > imc < 29.9:
    print('Resultado: Acima do peso.')
elif 30 > imc < 34.9:
    print('Resultado: Obesidade Grau I.')
else:
    print('Resultado: Peso normal.')