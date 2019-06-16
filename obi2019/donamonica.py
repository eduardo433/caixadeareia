"""
Dona Mônica tem três filhos. A soma da idade deles é igual à sua.

Dada a idade de DM e de dois filhos, calcular do terceiro
Entrada: Idade de Dona Mônica (M), Idade filho 1 (A), Idade filho 2 (B)

Saída: Idade filho 3 (C)

Restrições:
M = A + B + C / C = M - A - B
40 <= M <= 110
A < M
B < M
A != B

"""

def pega_idade(pessoa, minimo, maximo):
    idade = 0
    while idade < minimo or idade > maximo:
        entrada = input('Entre com a idade de %s, entre %d e %d (Ctrl+C sai)' %
                        (pessoa, minimo, maximo))
        try:
            idade = int(entrada)
        except ValueError:
            pass
    return idade

M = pega_idade('Dona Mônica', 40, 110)
A = pega_idade('Idade de um filho', 1, M)
B = A
while A == B:
    print('Atenção, idades dos filhos devem ser diferentes!')
    B = pega_idade('Idade de outro filho', 1, M - A)

C = M - A - B
print(C)

