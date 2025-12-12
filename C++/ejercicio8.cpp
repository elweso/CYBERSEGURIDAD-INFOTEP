#include <iostream>
using namespace std;

int main() {
    int numero;
    int suma = 0;
    
    cout << "Ingrese numeros (ingrese 0 para terminar):" << endl;
    
    while (true) {
        cout << "Numero: ";
        cin >> numero;
        
        if (numero == 0) {
            break;
        }
        
        suma += numero;
    }
    
    cout << "\nLa suma total de los numeros ingresados es: " << suma << endl;
    
    return 0;
}

