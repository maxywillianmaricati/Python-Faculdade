'''Nas cobranças de pênaltis em um jogo de futebol, cada time chuta uma vez por rodada. 
Se ambos os times marcarem gol ou se ambos os times errarem, uma nova rodada de chutes se inicia. Se um time marcar e o outro errar, vence quem marcou o gol.
Considerando a disputa de pênaltis entre o time A e B e 
que o time A sempre começa chutando, informe o resultado dos chutes 
na rodada e aponte quem venceu as cobranças de pênaltis ou reinicie 
a rodada até haver um vencedor.
Entrada
A entrada consiste em dois números inteiros referentes ao resultado
dos chutes na rodada, sendo o número 1 para indicar gol e o número 0 para indicar erro.
Saída
A SAÍDA consiste em um caractere com o nome do time vencedor: A ou B'''

while True:
    a = int(input())
    b = int(input())

    if a == 1 and b == 0:
        print('A')
        break
    elif a == 0 and b == 1:
        print('B')
        break
    elif a and b == 1:
        print('Empate!')
        continue
    elif a and b == 0:
        print('Nova rodada de chutes')
        continue