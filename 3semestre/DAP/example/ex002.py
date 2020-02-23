def contador(texto):

    dict = {}
    for palavra in texto.split(' '):
        if palavra in dict:
            dict[palavra] += 1
        else:
            dict[palavra] = 1
    return dict


textoA = "esse exercicio é um exercicio facil ou dificil"


print(contador(textoA))
