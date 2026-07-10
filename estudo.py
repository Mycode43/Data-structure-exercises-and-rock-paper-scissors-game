"""crie uma lista vazia;
peça 5 nomes;
mostre:
lista completa;
quantidade de nomes;
primeiro nome;
último nome."""
"""
nomes = []

n1 = input("Escreva o primeiro nome: ")
n2 = input("Escreva o segundo nome: ")
n3 = input("Escreva o terceiro nome: ")
n4 = input("Escreva o quarto nome: ")
n5 = input("Escreva o quinto nome: ")

nomes_list = [n1,n2,n3,n4,n5]

nomes.extend(nomes_list)
print(nomes)

print(len(nomes)) # nao usa indice aqui indice pega por posiçao a lista inteira se pega com parenteses mesmo!
print(nomes[0])
print(nomes[-1])
"""

#_________________________________________________________________________________________________________________

# exercicio 2

"""Crie um dicionário contendo:

nome
idade
cidade

infs = {"Nome": "Miguel",
        "idade": "13",
        "cidade": "Xique-xique Bahia (é zueira kkkkk)"}

print(infs)
"""

#__________________________________________________________________________________________________________________

"""🟡 Médio 1

Peça 10 números.

Guarde em uma lista.

Depois mostre:

maior número
menor número
soma
média

Sem usar sort()."""

"""
n1 = input("Digite o primeiro número: ")
n2 = input("Digite o segundo número: ")
n3 = input("Digite o terceiro número: ")
n4 = input("Digite o quarto número: ")
n5 = input("Digite o quinto número: ")
n6 = input("Digite o sexto número: ")
n7 = input("Digite o sétimo número: ")
n8 = input("Digite o oitavo número: ")
n9 = input("Digite o nono número: ")
n10 = input("Digite o décimo número: ")

numbers = [int(n1),int(n2),int(n3),int(n4),int(n5),int(n6),int(n7),int(n8),int(n9),int(n10)]

print(max(numbers))
print(min(numbers))
print(sum(numbers))

soma = sum(numbers) # sum nao e metodo de listas e sim funçoes do proprio python
quantidade = len(numbers) # len o mesmo de sum mas o sum é pra somar e o len pra mostrar a quantidade

print(soma / quantidade)
"""

"""
🟡 Médio 2

Peça uma frase.

Crie um dicionário que conte quantas vezes cada letra aparece.

Exemplo

banana

b = 1
a = 3
n = 2
"""

frase = input("Digita frase: ") # a variavel com a função input que faz com que o player possa escrever o texto

letras = {} # o dict vazio que sera preenchido com as letras e a quantidade delas

for letra in frase: # para cada letra na frase no player faça
    if letra in letras: 
        letras[letra] += 1
        print(letras)
    else:
        letras[letra] = 1
        print(letras)




