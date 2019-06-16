"""
Uma calçada tem N números V em sequência.

A sequência começa e termina com 1 e somente tem 1 ou 2 nela.

Calcular quantidade de números não iguais consecutivos.

Entrada: N, lista V

Saída: qtde diferentes consecutivos

Restricoes:
3 <= N <= 500
V em (1, 2)

"""


def pega_numero(minimo, maximo):
    numero = -1
    while numero < minimo or numero > maximo:
        entrada = input('Entre com um numero entrr %d e %d (Ctrl+C sai): ' %
                        (minimo, maximo))
        try:
            numero = int(entrada)
        except ValueError:
            pass
    return numero


def conta_consecutivos(sequencia):
    qtde = 0
    V_anterior = -1
    for V in sequencia:
        if V != V_anterior:
            qtde += 1
        print(V, V_anterior, qtde)
        V_anterior = V
    return qtde

print('Digite o tamanho da sequência.')
N = pega_numero(3, 500)
print(N)
sequencia = []
for ind in range(1, N + 1):
    if ind == 1 or ind == N:
        sequencia.append(1)
    else:
        print('Digite o item %d da sequencia.' % ind)
        sequencia.append(pega_numero(1, 2))

print('Sequência: %s' % sequencia)
print(conta_consecutivos(sequencia))