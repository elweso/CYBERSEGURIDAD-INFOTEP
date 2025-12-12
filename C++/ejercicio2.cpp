#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

int main() {
    string nombre;
    int edad;
    float estatura;
    
    cout << "Ingrese su nombre: ";
    getline(cin, nombre);
    
    cout << "Ingrese su edad: ";
    cin >> edad;
    
    cout << "Ingrese su estatura (en metros): ";
    cin >> estatura;
    
    cout << "\n========================================" << endl;
    cout << "           FICHA PERSONAL" << endl;
    cout << "========================================" << endl;
    cout << "Nombre:   " << nombre << endl;
    cout << "Edad:     " << edad << " anos" << endl;
    cout << fixed << setprecision(2);
    cout << "Estatura: " << estatura << " metros" << endl;
    cout << "========================================" << endl;
    
    return 0;
}

