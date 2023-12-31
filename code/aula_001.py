#!/usr/bin/env python3

print("Olá, mundo!")


# operadores aritmeticos
print(1 + 2)
print(1 - 2)
print(1 / 2)
print(1 * 2)

# e se eu fizer com strings?
print("Olá, " + "mundo" + "!")


# vars
nome = "Nassu"
print("Olá, " + nome + "!")
print("Como vai, " + nome + "?")
print("Ok beleza xau, " + nome + "!")

nome = "Nassu"
idade = 25
cidade = "Rio de Janeiro"
estado = "RJ"
casado = False
print(f"{nome} tem {idade} anos e mora em {cidade}, {estado}.")

# reatribuindo valores a uma mesma var
nome = "Nassu"
nome = "Tomas"
print(nome)

nome = 10
print(nome)


# recebendo input
nome = input("Qual é o seu nome?\n")
print(f"Olá, {nome}!")
print(type(nome))


# trabalhando com o tipo certo
idade = input("Qual é sua idade?\n")
print(type(idade))
print(type(26))

# descomentar essa linha pra ver que vai dar erro
# print(idade + 10)

# queremos que idade seja do tipo "int" para podermos usar a variavel como um número inteiro
idade = int(idade)
print(type(idade))
print(idade + 10)  # nao da erro


# condicionais
idade = int(input("qual é sua idade?\n"))

if idade >= 18:
    print("tome cachaça")
else:
    print("vá estudar, criança")

# elif
numero_sagrado = 41
chute = int(input("Tente adivinhar o número sagrado:\n"))

if chute == numero_sagrado:
    print("parabens você ganhou haha eba!")
elif chute > numero_sagrado:
    print("você chutou alto")
else:
    print("você chutou baixo")


# while
numero_sagrado = 41
acertou = False

while not acertou:
    chute = int(input("Tente adivinhar o número sagrado:\n"))

    if chute == numero_sagrado:
        print("parabens você ganhou haha eba!")
        acertou = True
    elif chute > numero_sagrado:
        print("você chutou alto")
    else:
        print("você chutou baixo")

# and
contador_chute = 0
numero_sagrado = 41
acertou = False

while not acertou and contador_chute < 10:
    chute = int(input("Tente adivinhar o número sagrado:\n"))
    contador_chute += 1

    if chute == numero_sagrado:
        print("parabens você ganhou haha eba!")
        acertou = True
    elif chute > numero_sagrado:
        print("você chutou alto")
    else:
        print("você chutou baixo")


# listas
nums = [32, 100, 2, -12, 4, 3, 5, 10, -50]
max_n = 32
i = 1
while i < len(nums):
    if nums[i] > max_n:
        max_n = nums[i]
    i += 1

print(max_n)


# for
nums = [32, 100, 2, -12, 4, 3, 5, 10, -50]
max_num = 32

for num in nums:
    if num > max_num:
        max_num = num

print(max_num)

# range
nums = [32, 100, 2, -12, 4, 3, 5, 10, -50]

for i in range(10):
    print(i)

for i in range(0, 10, 3):
    print(i)

for i in range(0, len(nums), 2):
    print(nums[i])


# funcoes
def ola_mundo():
    print("Olá, mundo!")


def contem(numeros, x):
    for num in numeros:
        if num == x:
            return True

    return False


def achar_max(numeros):
    max_num = numeros[0]

    for i in range(1, len(numeros)):
        if numeros[i] > max_num:
            max_num = numeros[i]

    return max_num


lista_a = [1, 2, 3]
lista_b = [-10, 50, 2]
print(contem(lista_a, 2))
print(contem(lista_b, 100))
print(achar_max(lista_a))
print(achar_max(lista_b))
