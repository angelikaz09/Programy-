#!/usr/bin/env python
# -*- coding: utf-8 -*-


def sort_wstaw(lista):
    """wersja liniowa"""
    for i in range(1, len(lista)):
        el = lista[i]
        k = i - 1
        while k >= 0 and lista[k] > el:  # wyszukuje pozycje do wstawienia
            lista[k + 1] = lista[k]  # przesuwanie elementów w góre tabeli
            k -= 1
        lista[k + 1] = el  # wstawianie elementu
    return lista


def wyszukaj_binarnie_it(lewy, prawy, lista, el):
    lewy, prawy = 0, len(lista) - 1
    while lewy < prawy:
        srodek = floor((lewy + prawy) / 2)
        # print (srodek)
        if el <= lista[srodek]:
            prawy = srodek
        else:
            lewy = srodek + 1

    if lista[lewy] == el:
        return lewy # znaleziono element

    return -1 # elementu nie znaleziono

def main(args):
    lista = [4, 3, 7, 0, 2, 3, 1, 9,]
    lista = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(lista)
    # [3, 4, 7, 0, 2, 3, 1, 9]
    # [3, 4, 7, 0, 2, 3, 1, 9]
    # [0, 3, 4, 7, 2, 3, 1, 9]
    print(sort_wstaw(lista))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
