#!/usr/bin/env python
# -*- coding: utf-8 -*-


def dec2other(liczba10, podstawa):
    """Konwersja liczby dziesiętnej na system o podanej podstawie"""
    liczba = []   # pusta lista do zapamiętywania reszt
    while liczba10 != 0:
        reszta = liczba10 % podstawa   # obliczanie reszt z dzielenia
        if reszta > 9:   # wykorzystanie kodu ASCII
            reszta = chr(reszta + 55)
        liczba.append(str(reszta))
        liczba10 = int(liczba10 / podstawa)

    liczba.reverse()   # odwrócenia kolejności elementów

    return "".join(liczba)


def zamiana1():
    """Pobranie danych wejściowych"""
    liczba = int(input("Podaj liczbę: "))
    podstawa = int(input("Podaj podstawę: "))
    while podstawa < 2 or podstawa > 16:
        podstawa = int(input("Podaj podstawę: "))
    print("Wynik konwersji: {}(10) = {}({})".format(
        liczba, dec2other(liczba, podstawa), podstawa))


def other2dec(liczba, podstawa):
    """Zamiana podanej liczby na system dziesiętny"""
    #  123(7) = 1 * 7^2 + 2 * 7^1 + 3
    liczba10 = 0
    potega = len(liczba) - 1
    for cyfra in liczba:
        if not cyfra.isdigit():
            liczba10 += (ord(cyfra.upper()) - 55) * (podstawa ** potega)

        else:
            liczba10 += int(cyfra) * (podstawa ** potega)
        potega -= 1

    return liczba10


def zamiana2():
    """Pobranie danych wejściowych"""
    liczba = input("Podaj liczbę: ")  # ABC
    podstawa = 0
    while podstawa < 2 or podstawa > 16:
        podstawa = int(input("Podaj podstawę: "))
    if podstawa > 9:
        for i in liczba:
            if ord(i) > 70:
                print("Zły format danych wejsciowych")
                return 0
    else:
        for i in liczba:
            if int(i) >= podstawa:
                print("Liczba nie moze skladac sie z cyfr > podstawy")
                return 0

    print("Wynik konwersji: {}({}) = {}(10)".format(
        liczba, podstawa, other2dec(liczba, podstawa)))


def main(args):
    print("Zamiana liczby dziesiętnej na liczbę o podanej podstawie "
          "<2;16> lub odwrotnie. ")
    # zamiana1()
    zamiana2()

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
