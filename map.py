''' 1. Crie uma função chamada quadrado(x) que retorna o quadrado de um número. 
    Depois use map() para gerar uma nova lista com os quadrados.'''

numeros = [1, 2, 3, 4, 5, 6, 7, 8]
def quadrado(numeros):
    return numeros ** 2

print(list(map(quadrado,numeros)))