'''import math

n = float(input())
print(f'fatorial de {n} é = {math.factorial(n)}')
print(f'floor de {n} é =  {math.floor(n)}')'''

frase = 'TADS 25 - Campus Itaituba'
tam = len(frase)
print(frase.upper().count('A')) #conta a quantidade de letras a
#print(frase.replace('a', 'u')) #substitui a por u
#.upper, .lower
print(frase.find('Campus')) #retorna a posição contando letra por letra
#print(frase.strip()) #remove o espaço branco no começo e no final
print('caqui' in frase) #retorna true ou false