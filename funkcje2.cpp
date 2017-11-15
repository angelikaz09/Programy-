/*
 * funkcje.cpp
 * 
 *
 * 
 */


#include <iostream>
using namespace std;

//int liczba =0; //zmienna globalna
//int krok =0; // zmienna lokalna

//~void zwieksz1 ()
//~{ 
    //~liczba +=krok
//~}

void zwieksz3 (int &liczba, int &krok) //przekazywanie przez wartość i przez referencje
{ 
    liczba +=krok;
    cout <<"Liczba"<< liczba << endl;
}

int main(int argc, char **argv)
{
    int liczba, krok; // zmienna lokalna 
    liczba = krok =0;
    
    cout <<"Podaj liczbę i krok"<< endl;
    cin >> liczba>> krok;
    
    cout<< &liczba <<  &krok << endl;
    
    zwieksz3 (liczba, krok);
    zwieksz3(liczba, krok);
    zwieksz3 (liczba, krok);
    
    
    cout <<"Liczba"<< liczba << endl;
    cout <<"Krok"<< krok << endl;
    
    return 0;
}

