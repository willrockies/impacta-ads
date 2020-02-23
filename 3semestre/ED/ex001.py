def defineMaximo(a, b):
    if a > b:
        print(a)
    else:
        print(b)


defineMaximo(1, 3)

print('\n')


def defineMaximo3(c, d, e):
    if c > d and c > e:
        print(c)
    elif d > c and d > e:
        print(d)
    else:
        print(e)


defineMaximo3(1, 2, 3)


def maximoLista(lista):
    maximo = lista[0]
       for valor in lista:
            if valor > maximo:
                maximo = lista
        return maximo
listao = [90, 91,78]
print(maximoLista())
