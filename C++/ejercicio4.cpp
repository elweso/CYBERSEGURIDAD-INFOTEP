#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    float base, altura, area;
    
    cout << "Ingrese la base del rectangulo: ";
    cin >> base;
    
    cout << "Ingrese la altura del rectangulo: ";
    cin >> altura;
    
    area = base * altura;
    
    cout << fixed << setprecision(2);
    cout << "\nEl area del rectangulo es: " << area << " unidades cuadradas" << endl;
    
    return 0;
}

