'''
###### 21) Média sem extremos ######
Leia números até o usuário digitar -1.

Calcule a média desconsiderando o maior e o menor valor digitados.

(Considere que o usuário digitará pelo menos 3 números válidos)
'''
#Max
nums = []
soma = 0
qtd = 0
sub = 0

while True:
    print('Digite -1 para parar')
    n = float(input('Digite o valor: '))
    
    if n == -1:
        print('Fim')
        break
    else:    
        nums.append(n)
        

qtd = len(nums)
menor = min(nums)
maior = max(nums)
nums.remove(maior)
nums.remove(menor)  
soma = sum(nums)
media = soma / qtd     

print(f'A media é: {media}')