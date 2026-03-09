'''Uma empresa de segurança recebeu duas listas:
    uma lista de usuários autorizados,
    e uma lista de usuários bloqueados.
Você deve ler uma terceira lista com tentativas de login e exibir somente os nomes dos usuários que podem acessar o sistema, ou seja:
estão na lista de autorizados, e não estão na lista de bloqueados.
Os nomes devem ser mostrados em ordem alfabética. Se nenhum nome for válido, exiba SEM ACESSO.
Entrada
    Lista de usuários autorizados (nomes separados por espaço).
    Lista de usuários bloqueados (nomes separados por espaço).
    Lista de tentativas de login (nomes separados por espaço).
Saída
Usuários autorizados, um por linha, em ordem alfabética. Se não houver, exiba SEM ACESSO.'''
autorizados = []
bloqueados = []
tentativas = []
#.sort() #ordenar em ordem alfabetica

a = input().split #autorizados
autorizados.append(a)

b = input().split #bloqueados
bloqueados.append(b)

nome = input().split #acesso ao sistema
tentativas.append(nome)

if nome in bloqueados:
    print('SEM ACESSO')