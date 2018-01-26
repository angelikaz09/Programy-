/*
 * dec2bin.cpp
 * 
 * 
 */


#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
    // dane wejściowe
    char znak A;
    char znak B;
    cout <<"Podaj liczbe i podstawe:";
    cin>>liczba;
    int liczba=;
    // 120-64=56
    // 56-32=24
    // 24-16=8
    // 8-8=0
    // 111100
    int podstawa=;
    
    // algorytm
    
    int i=0; // wskazuje ile reszt otrzymamy
    do { // petla wykona sie jeden raz 
        reszty [i] <<liczba%podstawa;
        liczba = liczba / podstawa;
        i++;
    } while(liczba>0);
    
    //~for (int  =i-1; j>=0; j--)
        //~cout<<reszty[j];
    //~}
   
    } while (i-1>=0)
        cout << reszty [i];
    }

	return 0;
}














