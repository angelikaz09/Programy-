/*
 * petle_cw.cxx
 * Program pobiera numer miesiąca i wyświetla jego nazwe
 * 
 */


#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
    char zn='t'; //deklaracja  
    
        while (true) {
            cout <<"Podaj znak";
            cin >>zn;
            if (zn == 't' || zn =='T' || zn =='n' || zn =='N')
               cout << zn << endl;
               else 
                   break;
            
            //switch (zn) 
            //{
                //case 't':
                //case 'T':
                //case 'n';
                //case 'N':
                    //cout << zn;
                //default 
                    //break
            //}
            
    };
    return 0;
}

