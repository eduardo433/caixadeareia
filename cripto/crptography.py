senha = 323
print(' para descodificar diga a senha')
digitado = int(input())
if digitado == senha:
    print('Digite uma mensagem ')
    mensagem = input()
    listadesimbolos = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
    cifra = 'abcdefghijklmnopqrstuvwxyz 1234567890'
    cifrada = ''
    inicio_numeros = cifra.find('1')
    for letra in mensagem.lower():
        indice = cifra.find(letra)
        # print(letra, indice)
        if indice > -1:
            if indice >= inicio_numeros:
                cifrada = cifrada + listadesimbolos[indice - inicio_numeros]
            else:
                cifrada = cifrada + '{:0>2}'.format(indice)

    print(cifrada)

    ind = 0
    decifrada = ''
    while ind < len(cifrada):
        if cifrada[ind] in listadesimbolos:
            decifrada = decifrada + cifra[listadesimbolos.index(cifrada[ind]) + inicio_numeros]
            ind += 1
        else:
            posicao_letra = int(cifrada[ind: ind + 2])
            # print(posicao_letra)
            decifrada = decifrada + cifra[posicao_letra]
            ind += 2

    print(decifrada)
