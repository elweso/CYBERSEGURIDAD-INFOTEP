#include <iostream>
#include <string>
using namespace std;

struct Estudiante {
    string nombre;
    int edad;
    float promedio;
};

int main() {
    Estudiante estudiantes[3];
    
    // Registrar 3 estudiantes
    for (int i = 0; i < 3; i++) {
        cout << "\n--- Estudiante " << (i + 1) << " ---" << endl;
        cout << "Nombre: ";
        cin.ignore();
        getline(cin, estudiantes[i].nombre);
        cout << "Edad: ";
        cin >> estudiantes[i].edad;
        cout << "Promedio: ";
        cin >> estudiantes[i].promedio;
    }
    
    // Encontrar el mejor promedio
    int indiceMejor = 0;
    float mejorPromedio = estudiantes[0].promedio;
    
    for (int i = 1; i < 3; i++) {
        if (estudiantes[i].promedio > mejorPromedio) {
            mejorPromedio = estudiantes[i].promedio;
            indiceMejor = i;
        }
    }
    
    // Mostrar el estudiante con mejor promedio
    cout << "\n========================================" << endl;
    cout << "   ESTUDIANTE CON MEJOR PROMEDIO" << endl;
    cout << "========================================" << endl;
    cout << "Nombre: " << estudiantes[indiceMejor].nombre << endl;
    cout << "Edad: " << estudiantes[indiceMejor].edad << " anos" << endl;
    cout << "Promedio: " << estudiantes[indiceMejor].promedio << endl;
    cout << "========================================" << endl;
    
    return 0;
}

