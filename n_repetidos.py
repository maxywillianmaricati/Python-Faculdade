'''Crie um programa que receba duas relações de números. Por fim deve ser exibido os números que ocorrem em ambos os conjuntos
Entrada
A primeira entrada correspondem aos números inteiros da primeira relação. Na segunda entrada deverão ser fornecidos os números da segunda relação de números inteiros.
Saída
Devem ser impressos os números repetidos, ou seja, números que existem na primeira e na segunda relação. 
Caso não exista números repetidos deve ser impresso a mensagem "Sem números repetidos!"'''

n1 = set(input().split())
n2 = set(input().split())

iguais = n1.intersection(n2)

if iguais:
    for numero in iguais:
        print(numero)
else:
    print('Sem números repetidos!')