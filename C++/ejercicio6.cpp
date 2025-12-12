#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

struct Producto {
    string nombre;
    float precio;
    int cantidad;
};

int main() {
    Producto productos[5];
    float valorTotal = 0;
    
    // Registrar 5 productos
    cout << "=== REGISTRO DE PRODUCTOS ===" << endl;
    for (int i = 0; i < 5; i++) {
        cout << "\n--- Producto " << (i + 1) << " ---" << endl;
        cout << "Nombre: ";
        cin.ignore();
        getline(cin, productos[i].nombre);
        cout << "Precio: ";
        cin >> productos[i].precio;
        cout << "Cantidad: ";
        cin >> productos[i].cantidad;
        
        // Calcular valor total del inventario
        valorTotal += productos[i].precio * productos[i].cantidad;
    }
    
    // Mostrar resumen
    cout << "\n========================================" << endl;
    cout << "        INVENTARIO DE PRODUCTOS" << endl;
    cout << "========================================" << endl;
    cout << left << setw(20) << "Producto" 
         << setw(15) << "Precio" 
         << setw(15) << "Cantidad" 
         << setw(15) << "Valor" << endl;
    cout << "----------------------------------------" << endl;
    
    cout << fixed << setprecision(2);
    for (int i = 0; i < 5; i++) {
        float valor = productos[i].precio * productos[i].cantidad;
        cout << left << setw(20) << productos[i].nombre
             << setw(15) << productos[i].precio
             << setw(15) << productos[i].cantidad
             << setw(15) << valor << endl;
    }
    
    cout << "========================================" << endl;
    cout << "VALOR TOTAL DEL INVENTARIO: $" << valorTotal << endl;
    cout << "========================================" << endl;
    
    return 0;
}

