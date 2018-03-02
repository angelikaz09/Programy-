/*
 * hello.cpp
 * 
 */


#include <iostream>
using namespace std;
int main(int argc, char **argv)
{
    // char imię; // deklaracja zmiennej znakowej
    char imie[10]; // deklaracja tablicy znakowej 
    int wiek; // deklaracja zmiennej typu całkowitego
    wiek=0; // inicjacja zmiennej 
    
	cout << "Witaj w C++" << endl; 
	cout << "Imie";
    //cin >> imię; 
    cin.getline(imie, 10);
    cout << "Cześć" << imie << endl;
    cout << "ile masz lat?"; 
    cin >> wiek;
    cout << "rok urodzenia" <<2017 - wiek << endl;
    
    
	return 0;
}

