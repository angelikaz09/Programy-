#!/usr/bin/env python
# -*- coding: utf-8 -*-


def zbadaj_liczbe(a):
    i = 2
    while a ==i: # while wykona się tylko dla 2
        i +=2
        if i > a:
            print(a, "nieparzyste")
            break
    print(a, "parzyste")

    return 0

     i = 2
     while a != i:
       i +=2
        if i > a:
            print(a, "nieparzyste")
            break
    if(i==a):
        print(a, "parzyste")
    return 0

def main(args):
    a = 0
    while a <= 0 or a >= 100:
        a = int(input))


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
