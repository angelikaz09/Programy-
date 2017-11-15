/*
 * kalkulator.cpp
 * 
 *
 * 
 * 
 */

#include <iostream> 
using namespace std;

int main(int argc, char **argv)
{
    char znak; // +, -, *, /
    
    cout <<"Podaj znak działania";
    cin >> znak ;
    int a,b;
    cout <<"Podaj dwie liczby";
    cin >> a >> b;
    
    if (znak == '+')
        cout <<"Wynik"<< a + b << endl;
    if (znak == '-')
        cout <<"Wynik"<< a - b << endl;
    if (znak == '*')
        cout <"Wynik"<< a * b << endl;
    if (znak == '/')
        cout <"Wynik"<< a / b << endl;
        
        
    return 0;
}

