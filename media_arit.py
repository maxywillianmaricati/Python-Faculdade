'''Escreva um programa que calcule a média aritmética de dois números inteiros fornecidos pelo usuário.
Entrada
A entrada consiste em dois números inteiros a e b
Saída
A saída deve ser a média aritmética dos dois números inteiros fornecidos.'''

a, b = map(int, input().split())
media = a + b / 2
print(f'RESULTADO: {media}')