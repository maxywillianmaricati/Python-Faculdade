'''
##### 16) Controle de estoque ######
Registrar entradas de produtos até digitar fim.

Para cada produto:
- nome
- quantidade

Ao final mostrar:
- total de itens adicionados
'''
# Max
nomes = []
qtd = []
c = 1

while c==1:
    print('\nCadastro de produto abaixo')
    p = input('Nome do produto: ')
    nomes.append(p)
    print(f'{p} foi inserido no estoque')
    
    
    print('\n0 para cancelar')
    print('1 para continuar')
    c = int(input('Deseja continuar adicionando itens?\n'))
    if c == 0:
        break
    elif c == 1:
        continue
    else:
        print('Digite algo válido!')
        break

total = len(nomes)
print(f'\nQuantidade de produtos adicionados: {total}')
print(f'Nome dos Produtos:{nomes}')