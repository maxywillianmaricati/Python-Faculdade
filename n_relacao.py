'''''Crie um programa que receba duas relações de números. Por fim devem ser exibidos os números que ocorrem na primeira mas não ocorrem na segunda relação.
Entrada
A  primeira entrada serão os números inteiros da primeira relação. A segunda entrada serão os números da segunda relação.
Saída
Na saída devem ser exibidos os números que ocorrem somente na primeira relação de números.
Caso todos os números da primeira relação ocorrerem na segunda, deve ser exibida a mensagem "todos os números ocorrem em ambos conjunto"'''

n1 = set(input().split())
n2 = set(input().split())

diferentes = n1.difference(n2)

if diferentes:
    for i in diferentes:
        print(i)
else:
    print('todos os números ocorrem em ambos conjunto')