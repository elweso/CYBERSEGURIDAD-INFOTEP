#include <iostream>
using namespace std;

int main() {
    int numero;
    
    cout << "Ingrese un numero para ver su tabla de multiplicar: ";
    cin >> numero;
    
    cout << "\nTabla de multiplicar del " << numero << ":" << endl;
    cout << "--------------------------------" << endl;
    
    for (int i = 1; i <= 12; i++) {
        cout << numero << " x " << i << " = " << (numero * i) << endl;
    }
    
    return 0;
}

