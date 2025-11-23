import random

opcao = ['pedra', 'papel', 'tesoura']
wins_jogador = 0
wins_computador = 0
rounds = 0

def jokenpo():
    global wins_jogador, wins_computador, rounds
    escolha = input('Você deseja jogar?[S/N]\n')

    if escolha == 'n':
        print('Você escolheu não jogar!')
        return
    
    if escolha != 's':
        print('Opção inválida.')
        return
    
    while escolha == 's':
        jogador = input('\nEscolha sua opção [ pedra, papel, tesoura ]\n')
        if jogador not in opcao:
                print('Escolha inválida!')
                return
        
        computador = random.choice(opcao)

        print(f'Você escolheu: {jogador}')
        print(f'O computador escolheu: {computador}')

        if jogador == computador:
                print('Empate!')
                print('Nenhum dos dois ganhou!')
                rounds += 1
        elif (jogador == 'pedra' and computador == 'tesoura') or \
                (jogador == 'papel' and computador == 'pedra') or \
                (jogador == 'tesoura' and computador == 'papel'):
                print('Você venceu!')
                wins_jogador += 1
                rounds += 1
        else:
                print('O computador venceu!')
                wins_computador += 1
                rounds += 1
        if rounds == 3:
              continuar = input('Quer continuar?(s/n)')
              if continuar == 'n':
                    break
              rounds = 0



        print('\n [ PLACAR ] ')
        print(f'Você possui {wins_jogador} vitórias!')
        print(f'O computador possui {wins_computador} vitórias!')

jokenpo()