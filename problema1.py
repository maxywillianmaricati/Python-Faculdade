''' A mãe de um colega abriu uma pequena loja de açaí no bairro. Ela anota tudo em um caderno, mas está se perdendo nos pedidos.
Cada cliente pode comprar quantos produtos quiser. O pedido só termina quando ela digita “0”.
Ela precisa de um programa simples que:

receba os pedidos
calcule o valor total
informe quantos itens foram comprados
informe se o cliente ganhou brinde (ganha se gastar mais de R$30) '''

print('\nBEM VINDO A LOJINHA DO ZED DO PIRACANÃ\nITENS A SEREM VENDIDOS:')
print('1. Açaí pequeno (R$ 10) \n2. Açaí médio (R$ 14)\n3. Açaí grande (R$ 18)\n4. Água (R$ 4)\n5. Refrigerante (R$ 6)')

carrinho = []
produtos = [
    {'escolha' :'1' ,'nome':'Açaí pequeno', 'preco':10},
    {'escolha' :'2' ,'nome':'Açaí médio','preco': 14},
    {'escolha' :'3' ,'nome':'Açaí grande','preco': 18},
    {'escolha' :'4' ,'nome':'Água','preco': 4},
    {'escolha' :'5' ,'nome': 'Refrigerante','preco': 6}
]


def adc_item(valor):
    escolhido = None
    for produto in produtos:
        if produto['escolha'] == valor:
            escolhido = produto
            break

    if escolhido is not None:
        carrinho.append(escolhido)
    else:
        print(f'\nitem nao encontrado!')

def pode_comprar():
    while True:
        escolha = input('\noque você deseja comprar?\ndigite 0 para encerrar:')
        
        if escolha == '0':
            break          
        
        adc_item(escolha)
        
        print('\nPEDIDO: ')
        for item in carrinho:
            print(f'{item['nome']} R${item['preco']}')
        
        

pode_comprar()