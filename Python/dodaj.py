#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
def sumuj(x,y):
    return x+y

def odejmij(x,y):
    return x-y
    

a= int(input ('Podaj liczbę')) 
b=int(input ('Podaj drugą liczbę'))
print ('suma', sumuj (a,b))
print ('roznica', odejmij (a,b))
