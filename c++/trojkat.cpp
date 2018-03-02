/*
 * trojkat.cpp
 * Program pobiera 3 boki trójkąta,
 * sprawdza czy da się z nich zbudować trójkąt,
 * oblicza obwód i pole (ze wzoru Herona),
 * i drukuje na ekranie odpowiedni komunikat 
 */


#include <iostream>
#include <math.h>
using namespace std;

int main(int argc, char **argv)
{
    int a, b, c;
    int obwod = 0;
    float p = 0;
    a = b = c =0;
         cout <<"Podaj boki trójkąta" << endl;
         cin >> a >> b >> c; 
         if ( a + b > c && a + c > b && b + c > a ) 
             {
                 obwod = a + b + c;
                 cout <<"Obwód"<< obwod << endl;
                 p = 0.5*obwod;
                 cout << "p = " << p << endl;
                 cout << "pole" << sqrt (p*(p-a)*(p-b)*(p-c));
             }   
    
	return 0;
}

