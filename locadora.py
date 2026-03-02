while True:
    total = 0
    inv = 19
    darko = 10
    aranha = 5
    ossos = 12
    carrinho = ''
    escolhido = None

    print('\n-=-=-=-=-=--=-=-=-=-=-')
    print('LOCADORA DE FILMES POGGERS')
    print('\nCATÁLOGO:\nSEÇÃO CDs')
    print('1- As vantagens de ser invisível | R$19')
    print('2- Donnie Darko | R$10')
    print('3- O espetacular Homen Aranha | R$5')
    print('4- Até os Ossos | R$12')
    print('-=-=-=-=-=--=-=-=-=-=-\n')

    print('Digite 0 para cancelar a compra')
    filme = int(input('Qual filme você gostaria de alugar?\n'))

    if filme == 1:
        tempo = int(input('Por quantos dias você quer alugar?'))
        total = tempo * inv
        print(f'Você adicionou o primeiro filme ao carrinho por {tempo} dias')
        escolhido == filme
        carrinho 

    elif filme == 2:
        tempo = int(input('Por quantos dias você quer alugar?'))
        total = tempo * darko
        print(f'Você adicionou o segundo filme ao carrinho{tempo} dias ')
        carrinho += 'Donnie Darko | R$10'
        
    elif filme == 3:
        tempo = int(input('Por quantos dias você quer alugar?'))
        total = tempo * aranha
        print(f'Você adicionou o terceiro filme ao carrinho{tempo} dias')
        carrinho += 'O espetacular Homen Aranha | R$5'

    elif filme == 4:
        tempo = int(input('Por quantos dias você quer alugar?'))
        total = tempo * ossos
        print(f'Você adicionou o quarto filme ao carrinho{tempo} dias')
        carrinho += 'Até os Ossos | R$12'
        

    elif filme == 0:
        print('Você cancelou a compra')
        print('Fim!')
        break

    else:
        print('\nEscolha um número válido que foi informado!')
        continue

    print('\nXXXXXXXXXXXXXXXXXXXXXX')
    print('CARRINHO:')
    print(f'{carrinho}, e o total a pagar é de {total}')
    print('XXXXXXXXXXXXXXXXXXXXXX\n')
