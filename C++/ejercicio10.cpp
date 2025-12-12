#include <iostream>
using namespace std;

int main() {
    int numero;
    int pares = 0;
    int impares = 0;
    
    cout << "Ingrese 10 numeros:" << endl;
    
    for (int i = 1; i <= 10; i++) {
        cout << "Numero " << i << ": ";
        cin >> numero;
        
        if (numero % 2 == 0) {
            pares++;
        } else {
            impares++;
        }
    }
    
    cout << "\n========================================" << endl;
    cout << "           RESULTADOS" << endl;
    cout << "========================================" << endl;
    cout << "Numeros pares: " << pares << endl;
    cout << "Numeros impares: " << impares << endl;
    cout << "========================================" << endl;
    
    return 0;
}

