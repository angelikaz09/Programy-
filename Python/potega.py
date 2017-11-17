#!/usr/bin/env python
# -*- coding: utf-8 -*-
# a0 = 1
# a1 = a
# an = a*......*a (n-czynników)

def potega_it(podst, wykladnik):
    """ Funkcja oblicza iteracyjnie potęgę l. naturalnej """
    wynik=1
    for i in range(wykładnik):
        wynik= wynik * podst
    return wynik


def main(args):
    # pobierz od użytkownika podstawe i wykładnik
    # i przypisz do odpowiednich zmiennych
    # wywołaj funkcje potega(it)
    a = int(input("Podaj podstawę:"))
    n = int(input("Podaj wykładnik:"))
    potega_it(a,n)
    assert type(a)==int
    assert type(n)==int

    assert potega_it(100, 0)==1
    assert potega_it(0, 100)==100
    assert potega_it(2, 3)==0

    ## print ("Potega:", potega_it(a,n))

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
