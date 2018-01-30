#!/usr/bin/env python
# -*- coding: utf-8 -*-


def dec2other(liczba10, podstawa):
    """Konwersja liczby dziesiętnej na system o podanej podstawie"""
    liczba = [] # pusta lista do zapamiętywania reszt
    while liczba10 != 0:
        reszta = liczba10 % podstawa # obliczanie resza z dzielenia
        if reszta > 9:
        liczba.append(str(reszta))
        liczba10 = int(liczba/podstawa) # uwaga
    liczba.reverse() # odwrócenie kolejności elementu
    return "".join(liczba)


def zamiana1():
    """Pobranie danych wejściowych"""
    liczba = int(input("Podaj liczbę:")
    podstawa = 0
    while podstawa < 2 or podstawa > 16:
        podstawa = int(input("Podaj podstawę: "))
    print ("wynik konwersji: {}(10) = {}({})" .format(liczba, dec2other (liczba, podstawa), podstawa))


def zamiana2():
    """Pobranie danych wejściowych"""
    liczba = (input("Podaj liczbę:")
    podstawa = 0
    while podstawa < 2 or podstawa > 16:
        podstawa = int(input("Podaj podstawę: "))
    print ("wynik konwersji: {}(10) = {}({})" .format(liczba, other2dec (liczba, podstawa), podstawa))

def other2dec():
    """Zamiana podanej liczby na system dziesiętny"""


def main(args):
    print ("Zamiana liczby dziesiętnej na liczbę o podanej podstawie ")
            "<2;16> lub odwrotnie.")
    zamiana1()
    return 0



if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
