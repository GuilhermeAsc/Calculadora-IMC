#Calculadora IMC
#By asC-_


nome = input(f'Digite seu Nome: ')
idade = float(input(f'Digita sua idade: '))
peso = float(input(f'Digite seu peso(em Kg): '))
altura = float(input(f'Digite sua altura(Em metros): '))

imc = peso/altura**2

if imc <= 18.5:
    print(f'Você está abaixo do peso pois está com um imc de: {imc}')
elif imc <= 24.9:
    print(f'Você está no seu peso ideal e seu imc é de: {imc}')
elif imc <= 29.9:
    print(f'Seu IMC é de {imc} e você está levemente acima do peso')
      