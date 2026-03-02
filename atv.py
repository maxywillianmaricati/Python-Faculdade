p = 4
compras = []
valor = []
media = 0
qtd = 0
total = 0
n = 4

while(p==4):
    print('\n---------------------------------')
    print('VENDINHA DE SKINS VANDAL')
    print('\n OPÇÕES DISPONIVEIS NA LOJA')
    print('1- KURONAMI R$2000 \n2- PRELUDIO DO CAOS R$1200 \n3- SAQUEADORA R$1500')
    print('---------------------------------')
    print('digite 0 para encerrar')

    #qtd de itens no carrinho        
    qtd = len(compras)
    #media
    md = sum(valor)
    #total a pagar
    total = sum(valor)
    
    if qtd == 3:
        print('voce já adicionou todos os itens existentes ao carrinho')
        break
    elif qtd == 0:
        n = int(input('escolha [1, 2 ,3]: '))
    elif qtd == 1 or 2:
        p = int(input('deseja comprar mais alguma? [0, 4]: '))
        if p == 0:
            print('fim')
            break
        elif p == 4:
            n = int(input('escolha [1, 2 ,3]: '))
        
    if n == 1:
        print('voce escolheu a kuronami')
        compras.append('KURONAMI')
        valor.append(2000)
        qtd + 1
    elif n ==2:
        print('voce escolheu a preludio do caos')
        compras.append('PRELUDIO DO CAOS')
        valor.append(1200)
        qtd + 1
    elif n == 3:
        print('voce escolheu a saqueadora')
        compras.append('SAQUEADORA')
        valor.append(1500)
        qtd +1
                
    print(print('\n---------------------------------'))
    print('COMPRAS NO CARRINHO:')
    print(compras, valor)
    print(f'\nMENOR VALOR: {min(valor)}')
    print(f'MAIOR VALOR: {max(valor)}')
    print(f'MEDIA DE VALOR: {media}')
    print(f'QUANTIDADE DE SKINS NO CARRINHO: {qtd}')
    print(f'TOTAL A PAGAR: {total}')
    print('---------------------------------\n')