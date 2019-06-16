
def DecifrarECriptografar():
    senha1 = 'dudu4'
    print('digite  a senha')
    digitado1 = input()
    if digitado1 == senha1:
       print('Digite uma mensagem ')
       mensagem = input()
       listadesimbolos = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
       cifra = 'abcdefghijklmnopqrstuvwxyz 1234567890'
       cifradeletras ='lcyrjpdoavzhbktxgswufeminq '
       cifrada = ''
       inicio_numeros = cifra.find('1')
       inicio_letras = cifra.find('a')
       for letra in mensagem.lower():
            indice = cifra.find(letra)
        # print(letra, indice)
            if indice > -1:
                if indice >= inicio_numeros:
                     cifrada = cifrada + listadesimbolos[indice - inicio_numeros]
                else:
                     cifrada = cifrada + cifradeletras[indice - inicio_letras]
            import os
            os.system('clear')
            print(cifrada)
    senha = 323
    ind = 0
    decifrada = ''
    print(' para descodificar diga a senha')
    digitado = int(input())
    if digitado == senha:
        while ind < len(cifrada):
             if cifrada[ind] in listadesimbolos:
                 decifrada = decifrada + cifra[listadesimbolos.index(cifrada[ind]) + inicio_numeros]
                 ind += 1
             else:
                 decifrada = decifrada + cifra[cifradeletras.index(cifrada[ind]) + inicio_letras]
                 ind += 1
            #posicao_letra = int(cifrada[ind: ind + 2])
            # print(posicao_letra)
            #decifrada = decifrada + cifra[posicao_letra]
            #ind += 2
        print(decifrada)

    else:
          exit('vocẽ errou' )
    print('deseja continuar')
    pergunta = input()
    if pergunta == 's' or 'sim':
        DecifrarECriptografar()
DecifrarECriptografar()

