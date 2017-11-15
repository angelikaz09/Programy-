#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint


def losuj(ileliczb, maksliczb):
    liczby=[]
    ile=0  # ilość wylosowanych liczb
    while ile<ileliczb:
    # for i in range(ileliczb):
        liczba=randint(0,maksliczb)
        if liczby.count(liczba)==0:
            liczby.append(liczba)
            ile +=1
    return liczby


def pobierz_typy():

def main(args):
    ileliczb=int(input("lle liczb chcesz zgadnąć?"))
    maksliczb=int(input("Podaj górny zakres:"))

    while ileliczb>maksliczb
        ileliczb int
            input("lle liczb chcesz zgadnąć z %s?" % maksliczb))


    liczby = losuj(ileliczb, maksliczb)
    typy = pobierz_typy(ileliczb)

    trafione = set(liczby)+
    print (trafione)





    return typy

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
