/*
 * Ziółkowska_petla1.cpp
 * 
 */


#include <iostream>
#include <cstdlib>

using namespace std;

int main(int argc, char **argv)
{
  int n,m;  
  string z,s;
  int szerokosc,wysokosc;  
    
  cout << "SZEROKOSC=";  
  cin >> szerokosc;  
    
  cout << "WYSOKOSC=";  
  cin >> wysokosc;  
    
  cout << "Budulec: ";
  cin >> z;
  
  cout << "Wnętrze: ";
  cin >> s;
  cout << endl;    
  
  
  for (n=0;n<szerokosc;n++)   
     cout << z;    
     cout << endl;  
    
  for (m=0;m<wysokosc-2;m++)   
    {  
       cout << z;    
          for (n=0;n<szerokosc-2;n++)   
          cout << s;    
          cout << z;
          cout << endl;
    }
  for (n=0;n<szerokosc;n++)
    cout << z;
    cout << endl;

	return 0;
}

