# Você tem um conjunto de eleitores,
# um conjunto de candidatos
# e o total de votos por candidato
from collections import defaultdict


def identifica_eleitor(eleitores):
    '''Recebe do teclado o nome do eleitor.

    Recebe do teclado o nome do eleitor e verifica se está na lista de
     eleitores e retorna o nome dele. Se a lista de eleitores ficar vazia,
     retorna None.
    '''
    if len(eleitores) == 0:
        return None
    while True:
        nome = input('Eleitor, identifique-se digitando seu nome: ')
        if nome in eleitores:
            eleitores.discard(nome)
            return nome
        else:
            print()
            print('Nome inválido!')
            print('Eleitores que ainda náo votaram:', ', '.join(eleitores))


def registra_votacao(eleitor_atual, candidatos):
    '''Exibe candidatos para o eleitor atual e registra voto.'''
    if len(candidatos) == 0:
        return None
    while True:
        print('Bem vindo à votação, %s' % eleitor_atual)
        nome = input('Escolha seu candidato: %s ' % candidatos)
        if nome in candidatos:
            votacao_candidato[nome] += 1
            print('### VOTAÇÃO ENCERRADA PARA %s ###' % eleitor_atual)
            return True
        else:
            print()
            print('Nome inválido!!!! Digite o nome de um candidato.')
            print()


def imprime_votacao():
    for k, v in votacao_candidato.items():
        print('Candidato: %s  Votos: %s' % (k, v))


candidatos = set(('Dudu', 'Felipe'))
eleitores = set(('Ivan', 'Amanda')) | candidatos
votacao_candidato = defaultdict(int)
eleitor_atual = ''
while eleitor_atual is not None:
    eleitor_atual = identifica_eleitor(eleitores)
    if eleitor_atual:
        registra_votacao(eleitor_atual, candidatos)

imprime_votacao()
