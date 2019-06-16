"""
Jogo dominó duplo-N
Receber uma entrada 0 <= N <= 10000
Calcular o número de combinações ((N+1)*(N+2)/2

"""
def peçasdedominó():
    entrada = input('Digite um numero entre 0 e 10.000 (Enter para sair): ')
    N = -1
    try:
        N = int(entrada)
    except ValueError:
        pass
    if N < 0 or N > 10000:
        print('O número deve estar entre 0 e 10000. Saindo...')
        exit(0)
    combinacoes_possiveis = ((N + 1) * (N + 2) / 2)
    print('O número de combinações em um jogo duplo-N é: %d' % combinacoes_possiveis)
    x = input('deseja continuar ')
    if x == "sim":
        peçasdedominó()
    elif x !='sim':
        exit()

peçasdedominó()
