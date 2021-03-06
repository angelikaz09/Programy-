#!/usr/bin/env python
# -*- coding: utf-8 -*-


def fib_rek(n):
    if n == 1:
        return 1
    return fib_rek()




def fib_iter(n):
    """funkcja wyświetla kolejne wyrazy ciągu fibonacciego
    funkcja zwraca n-ty wyraz ciągu
    F(0) = 0
    F(1) = 1
    F(n) = F(n-2) + F(n-2) dla n > 1
    """

    a, b = (0, 1)
    if n == 0:
        print (a)
        return a
    # elif n == 1:
    #      print (b)
    #      return b

    print (a)
    print (b)
    for i in range(2, n):
        tmp = b
        b = a + b
        a = tmp
        a, b = b, a + b
        print (a, " wyraz ", i, ": ", b)

    return b


def fib_iter2(n):

    a, b = (0, 1)

    print (a)
    while n > 0:
         a, b = b, a + b
        print (a, ": ", b, "iloraz:", b / a)
        n = n - 1

    return b


def main(args):
    fib_iter(10)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
