'''Escreva um programa que solicite, continuamente, números inteiros. Caso algum número fornecido seja ímpar, o programa deve encerrar.
Entrada
Números inteiros, positivos ou negativos.
Saída
Antes do encerramento do programa deve ser exibido uma mensagem, conforme o exemplo abaixo.'''

while True:
    num = int(input())
    if num % 2 == 0:
        continue
    else:
        print('Encerrando o programa...')
        break