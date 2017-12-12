#!/usr/bin/env python
# -*- coding: utf-8 -*-


def silnia_rek(n):
    if n < 2:
        return 1
    return silnia_rek(n-1)*n



def silnia_it(n):
    """ Funkcja oblicza iteracyjnie silnię l. naturalnej """
    wynik = 1
    for i in range(2, n+1):
        wynik = wynik * i
    return wynik


def main(args):
    a = int(input("Podaj liczbe:"))
    assert type(a)==int

    assert silnia_it (0) == 1
    assert silnia_it (1) == 1
    assert silnia_it (7) == 5040
    assert silnia_rek (7) == 5040
    print ("Silnia: ", silnia_rek(n))




    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
