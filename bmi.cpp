/*
 * bmi.cpp
 * 
 * 
 * 
 */

#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
    float waga;
    float wzrost;
    float bmi;
    waga = wzrost = bmi = 0;
    
    cout <<"Podaj wagę (kg)!" << endl;
    cin >> waga;
    cout <<"Podaj wzrost (m)!" << endl;
    cin >> wzrost;
    
    bmi = (waga/(wzrost*wzrost));
    
    cout << bmi << endl;
    
    if (bmi < 18.5) 
    {
    cout <<"Niedowaga"<< endl; 
    }
    else if (bmi >= 18.5 && bmi < 25)
    {
        cout <<"Norma"<< endl;
    }
        else if (bmi >= 25 && bmi <30)
    {
        cout <<"Nadwaga"<< endl;
    }
    else cout <<"Otyłość"<< endl;
        
	return 0;
}

