#DATA: 09/05/2025


#Peça ao usuário para digitar 5 números e mostre a soma final deles:

numero1 = int (input('Digite o primeiro número: '))
numero2 = int (input('Digite o segundo número: '))
numero3 = int (input('Digite o terceiro número: '))
numero4 = int (input('Digite o quarto número: '))
numero5 = int (input('Digite o quinto número: '))

soma = numero1 + numero2 + numero3 + numero4 + numero5

print ('A soma dos 5 números é 'f'{soma}')


#Peça ao usuário para digitar 4 números e mostre qual é o maior e qual é o menor: 

numero1 = int (input('Digite o primeiro número: '))
numero2 = int (input('Digite o segundo número: '))
numero3 = int (input('Digite o terceiro número: '))
numero4 = int (input('Digite o quarto número: '))

ListaNumeros = [numero1, numero2, numero3, numero4]

ListaNumeros.sort (reverse =False)

print(f'O menor número digitado é {ListaNumeros[0]} \nO maior número digitado é {ListaNumeros[-1]}')

#Peça ao usuário uma palavra e mostre quantas vogais ela tem.

palavra = input('Digite uma palavra: ')
vogais = ["a", "e", "i", "o", "u"]
contador = 0

for letra in palavra:
    for vogal in vogais:
        if(vogal == letra):
            contador += 1
print(f"A palavra {palavra} tem {contador} vogais")

#Peça ao usuário para digitar 6 números e mostre apenas os números pares digitados.

numero1 = int (input('Digite o primeiro número: '))
numero2 = int (input('Digite o segundo número: '))
numero3 = int (input('Digite o terceiro número: '))
numero4 = int (input('Digite o quarto número: '))
numero5 = int (input('Digite o quinto número: '))
numero6 = int (input('Digite o sexto número: '))

ListaNumeros = [numero1, numero2, numero3, numero4, numero5, numero6]
contador = 0
for numero in ListaNumeros: 
   if (numero %2 == 0):
    contador += 1
print(f"Entre os números digitados, {contador} deles são pares")

#Solicite as notas de 3 provas e mostre a média.

nota1 = float (input(f"Digite a primeira nota: "))
nota2 = float (input(f"Digite a segunda nota: "))
nota3 = float (input(f"Digite a terceira nota: "))

somaNotas = nota1 + nota2 + nota3
media = somaNotas/3
print (f"A sua média é {media}")

#Peça ao usuário um número e mostre a tabuada desse número de 1 a 10.

numero = int (input(f"Digite um número: "))

contador = 1

while contador <= 10:
    print (f"{numero} X {contador} = {numero * contador}")
    contador += 1

#Peça um número N ao usuário e mostre todos os números de 1 até N.


#Peça ao usuário uma palavra e mostre ela ao contrário.
#Peça um número ao usuário e diga se ele é múltiplo de 3.
#Peça ao usuário para digitar 3 nomes e mostre todos eles em ordem alfabética.
