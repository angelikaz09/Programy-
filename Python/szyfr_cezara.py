#!/usr/bin/env python
# -*- coding: utf-8 -*-


def szyfruj(tekst,klucz):
    """Szyfrowanie za pomocą szyfru cezara"""
    szyfrogram = ""
    klucz = klucz%26
    for znak in tekst:
        ascii = ord(znak) + klucz
        if ascii > 90:
            ascii - 26
        szyfrogram += chr(ascii)
    return szyfrogram


def main(args):
    tekst = int(input("Podaj tekst:"))
    klucz = int(input("POdaj klucz:"))
    szyfrogram = szyfruj(tekst, klucz)
    print(szyfrogram)


def deszyfruj(szyfrogram, klucz):


    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
