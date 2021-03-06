#!/usr/bin/env python
# -*- coding: utf-8 -*-
# a0 = 1
# a1 = a
# an = a*......*a (n-czynników)


def potega_it(podst, wykladnik):
    """ Funkcja oblicza iteracyjnie potęgę l. naturalnej """
    wynik = 1
    for i in range(wykladnik):
        wynik = wynik * podst
    return wynik


# a0 = 1 warunek brzegowy
# an = a(n-1) * a dla n > 0


def potega_rek(a, n):
    if n == 0:
        return 1
    return potega_rek(a, n-1) * a




def main(args):

    a = int(input("Podaj podstawe:"))
    n = int(input("Podaj wykladnik:"))

    assert type(a) == int
    assert type(n) == int

    assert potega_it(100, 0) == 1
    assert potega_it(100, 1) == 100
    assert potega_it(2, 3) == 8
    assert potega_rek(2, 3) == 8

   ("potega: ", potega_rek(a, n))

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
