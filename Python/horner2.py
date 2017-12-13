#!/usr/bin/env python
# -*- coding: utf-8 -*-


def horner_rek(k, tbwsp, x):
    wynik = tbwsp[0]
    for i in range(1, k + 1):
        wynik = wynik * x + tbwsp[i]
        return wynik


def main(args):
    tbwsp = []
    stopien = 3
    x = int(input("Podaj argument: "))
    for i in range(0, 4):
        tmp = int(input("Podaj współczynnik: "))
        tbwsp.append(tmp)

    print("Wynik ", horner_it(stopien, tbwsp, x))

    return 0


if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
