#Calculadora IMC
#By asC-_

nome = input(f'Digite seu Nome: ')
idade = float(input(f'Digita sua idade: '))
peso = float(input(f'Digite seu peso(em Kg): '))
altura = float(input(f'Digite sua altura(Em metros): '))

imc = peso/altura**2

if imc <= 18.5:
    print(f'Seu IMC é de {imc} e você está abaixo do peso')
elif imc <= 24.9:
    print(f'Seu IMC é de {imc} e você está com o peso ideal')
elif imc <= 29.9:
    print(f'Seu IMC é de {imc} e você está levemente acima do peso')
elif imc <= 34.9:
    print(f'Seu IMC é de{imc} e você está com obesidade grau I')
elif imc <= 39.9:
    print(f'Seu IMC é de {imc} e você está com obesidade grau II')
else:
    print(f'Seu IMC é de {imc} e você está com obesidade grau III')