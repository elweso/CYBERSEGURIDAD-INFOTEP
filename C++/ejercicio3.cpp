#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    float celsius, fahrenheit;
    
    cout << "Ingrese la temperatura en grados Celsius: ";
    cin >> celsius;
    
    // Formula: F = (C * 9/5) + 32
    fahrenheit = (celsius * 9.0 / 5.0) + 32;
    
    cout << fixed << setprecision(2);
    cout << "\n" << celsius << " grados Celsius equivalen a " 
         << fahrenheit << " grados Fahrenheit" << endl;
    
    return 0;
}

