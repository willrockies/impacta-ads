import unittest


def troca(lista, pos1, pos2):
    aux = lista[pos1]
    lista[pos1] = lista[pos2]
    lista[pos2] = aux

    return lista


troca([2, 23, 12, 76, 21, 96], 1, 16)
