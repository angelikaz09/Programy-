<<<<<<< HEAD
#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main(args):
        n = 0
    while n < 2:
        n = int(input("Podaj liczbę: "))


=======
/*
 * zad_1_algorytm.py
 * 
 * 
 */

def main(args):
    n = 0
    while n < 2:
        n = int(input("Podaj liczbę: "))
        
        
>>>>>>> 6f88ec87bd69bb90f9e430ebbb231042a43baf98
    i = 2
    while i * i <= n:
        if n % i == 0:
            print("Liczba złożona!")
            return 0
        i += 1
    print("Liczba pierwsza!")
<<<<<<< HEAD

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
=======
    
    
    return 0

if __name__ == '__main__':
    import sys
sys.exit(main(sys.ar
>>>>>>> 6f88ec87bd69bb90f9e430ebbb231042a43baf98
