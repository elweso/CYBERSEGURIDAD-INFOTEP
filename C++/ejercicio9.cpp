#include <iostream>
using namespace std;

int main() {
    int opcion;
    float num1, num2, resultado;
    
    do {
        cout << "\n========================================" << endl;
        cout << "            MENU CALCULADORA" << endl;
        cout << "========================================" << endl;
        cout << "1. Sumar" << endl;
        cout << "2. Restar" << endl;
        cout << "3. Multiplicar" << endl;
        cout << "4. Salir" << endl;
        cout << "========================================" << endl;
        cout << "Seleccione una opcion: ";
        cin >> opcion;
        
        if (opcion >= 1 && opcion <= 3) {
            cout << "\nIngrese el primer numero: ";
            cin >> num1;
            cout << "Ingrese el segundo numero: ";
            cin >> num2;
            
            switch (opcion) {
                case 1:
                    resultado = num1 + num2;
                    cout << "\nResultado: " << num1 << " + " << num2 << " = " << resultado << endl;
                    break;
                case 2:
                    resultado = num1 - num2;
                    cout << "\nResultado: " << num1 << " - " << num2 << " = " << resultado << endl;
                    break;
                case 3:
                    resultado = num1 * num2;
                    cout << "\nResultado: " << num1 << " * " << num2 << " = " << resultado << endl;
                    break;
            }
        } else if (opcion == 4) {
            cout << "\n¡Hasta luego!" << endl;
        } else {
            cout << "\nOpcion invalida. Por favor, seleccione una opcion del 1 al 4." << endl;
        }
        
    } while (opcion != 4);
    
    return 0;
}

