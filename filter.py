'''Crie uma função chamada maior_que_4(x) que retorna True se o número for maior que 4.
Use filter() para gerar uma lista apenas com esses valores.'''

numeros = [1, 2, 3, 4, 5, 6, 7, 8]

def maior_que_4(numeros):
    return numeros > 4
        
print(list(filter(maior_que_4,numeros)))