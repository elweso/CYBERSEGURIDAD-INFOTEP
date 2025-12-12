#include <iostream>
using namespace std;

int main() {
    int num1, num2;
    
    cout << "Ingrese el primer numero entero: ";
    cin >> num1;
    
    cout << "Ingrese el segundo numero entero: ";
    cin >> num2;
    
    cout << "\nResultados:" << endl;
    cout << "Suma: " << num1 << " + " << num2 << " = " << (num1 + num2) << endl;
    cout << "Resta: " << num1 << " - " << num2 << " = " << (num1 - num2) << endl;
    cout << "Multiplicacion: " << num1 << " * " << num2 << " = " << (num1 * num2) << endl;
    
    if (num2 != 0) {
        cout << "Division: " << num1 << " / " << num2 << " = " << (static_cast<float>(num1) / num2) << endl;
    } else {
        cout << "Division: No se puede dividir por cero" << endl;
    }
    
    return 0;
}

