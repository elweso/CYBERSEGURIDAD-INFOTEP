#include <iostream>
#include <vector>
#include <string>
#include <iomanip>
#include <algorithm>
#include <ctime>
#include <sstream>
using namespace std;

// Estructura para representar un dispositivo
struct Dispositivo {
    string mac;
    string ip;
    string nombre;
    bool autorizado;
    bool conectado;
    int horaConexion;
    int minutoConexion;
};

// Estructura para alertas
struct Alerta {
    string tipo;
    string mensaje;
    string dispositivo;
    string hora;
};

// Variables globales
vector<Dispositivo> dispositivos;
vector<Alerta> alertas;
const int MAX_CONEXIONES_SIMULTANEAS = 5;
const int MAX_DISPOSITIVOS = 100;

// Prototipos de funciones
void mostrarMenu();
void registrarDispositivo();
void validarAcceso();
void generarAlertas();
void mostrarDispositivos();
void mostrarConexionesActivas();
void mostrarAlertas();
bool validarFormatoMAC(const string& mac);
bool validarFormatoIP(const string& ip);
bool dispositivoExiste(const string& mac);
int contarConexionesActivas();
string obtenerHoraActual();
void desconectarDispositivo();

int main() {
    int opcion;
    
    cout << "========================================" << endl;
    cout << "   SISTEMA DE CONTROL DE ACCESOS WiFi" << endl;
    cout << "========================================" << endl;
    cout << "Limite de conexiones simultaneas: " << MAX_CONEXIONES_SIMULTANEAS << endl;
    cout << "========================================\n" << endl;
    
    do {
        mostrarMenu();
        cout << "Seleccione una opcion: ";
        cin >> opcion;
        cin.ignore(); // Limpiar buffer
        
        switch (opcion) {
            case 1:
                registrarDispositivo();
                break;
            case 2:
                validarAcceso();
                break;
            case 3:
                generarAlertas();
                break;
            case 4:
                mostrarDispositivos();
                break;
            case 5:
                mostrarConexionesActivas();
                break;
            case 6:
                mostrarAlertas();
                break;
            case 7:
                desconectarDispositivo();
                break;
            case 8:
                cout << "\nSaliendo del sistema..." << endl;
                break;
            default:
                cout << "\nOpcion invalida. Intente nuevamente." << endl;
        }
        
        if (opcion != 8) {
            cout << "\nPresione Enter para continuar...";
            cin.get();
        }
        
    } while (opcion != 8);
    
    return 0;
}

void mostrarMenu() {
    cout << "\n========================================" << endl;
    cout << "              MENU PRINCIPAL" << endl;
    cout << "========================================" << endl;
    cout << "1. Registrar Dispositivo" << endl;
    cout << "2. Validar Acceso (Conectar)" << endl;
    cout << "3. Generar Alertas" << endl;
    cout << "4. Mostrar Dispositivos Registrados" << endl;
    cout << "5. Mostrar Conexiones Activas" << endl;
    cout << "6. Mostrar Alertas" << endl;
    cout << "7. Desconectar Dispositivo" << endl;
    cout << "8. Salir" << endl;
    cout << "========================================" << endl;
}

// Función para validar formato MAC (XX:XX:XX:XX:XX:XX)
bool validarFormatoMAC(const string& mac) {
    if (mac.length() != 17) return false;
    
    for (int i = 0; i < 17; i++) {
        if (i % 3 == 2) {
            if (mac[i] != ':') return false;
        } else {
            if (!isxdigit(mac[i])) return false;
        }
    }
    return true;
}

// Función para validar formato IP básico (X.X.X.X)
bool validarFormatoIP(const string& ip) {
    int puntos = 0;
    string numero = "";
    
    for (char c : ip) {
        if (c == '.') {
            if (numero.empty() || stoi(numero) > 255) return false;
            puntos++;
            numero = "";
        } else if (isdigit(c)) {
            numero += c;
        } else {
            return false;
        }
    }
    
    if (puntos != 3 || numero.empty() || stoi(numero) > 255) return false;
    return true;
}

// Función para verificar si un dispositivo ya existe
bool dispositivoExiste(const string& mac) {
    for (const auto& dispositivo : dispositivos) {
        if (dispositivo.mac == mac) {
            return true;
        }
    }
    return false;
}

// Función para obtener hora actual
string obtenerHoraActual() {
    time_t ahora = time(0);
    tm* tiempo = localtime(&ahora);
    
    stringstream ss;
    ss << setfill('0') << setw(2) << tiempo->tm_hour << ":"
       << setfill('0') << setw(2) << tiempo->tm_min;
    return ss.str();
}

// Función para contar conexiones activas
int contarConexionesActivas() {
    int contador = 0;
    for (const auto& dispositivo : dispositivos) {
        if (dispositivo.conectado) {
            contador++;
        }
    }
    return contador;
}

// Función 1: Registrar Dispositivo
void registrarDispositivo() {
    cout << "\n========================================" << endl;
    cout << "      REGISTRAR NUEVO DISPOSITIVO" << endl;
    cout << "========================================" << endl;
    
    if (dispositivos.size() >= MAX_DISPOSITIVOS) {
        cout << "ERROR: Se ha alcanzado el limite maximo de dispositivos." << endl;
        return;
    }
    
    Dispositivo nuevo;
    
    // Solicitar MAC
    cout << "Ingrese la direccion MAC (formato: XX:XX:XX:XX:XX:XX): ";
    getline(cin, nuevo.mac);
    
    // Validar formato MAC
    if (!validarFormatoMAC(nuevo.mac)) {
        cout << "ERROR: Formato de MAC invalido. Use el formato XX:XX:XX:XX:XX:XX" << endl;
        return;
    }
    
    // Verificar si ya existe
    if (dispositivoExiste(nuevo.mac)) {
        cout << "ERROR: Este dispositivo ya esta registrado." << endl;
        return;
    }
    
    // Solicitar IP
    cout << "Ingrese la direccion IP (formato: X.X.X.X): ";
    getline(cin, nuevo.ip);
    
    // Validar formato IP
    if (!validarFormatoIP(nuevo.ip)) {
        cout << "ERROR: Formato de IP invalido. Use el formato X.X.X.X" << endl;
        return;
    }
    
    // Solicitar nombre
    cout << "Ingrese el nombre del dispositivo: ";
    getline(cin, nuevo.nombre);
    
    // Solicitar autorización
    char autorizado;
    cout << "¿Esta autorizado? (S/N): ";
    cin >> autorizado;
    nuevo.autorizado = (autorizado == 'S' || autorizado == 's');
    
    nuevo.conectado = false;
    nuevo.horaConexion = 0;
    nuevo.minutoConexion = 0;
    
    dispositivos.push_back(nuevo);
    
    cout << "\n✓ Dispositivo registrado exitosamente!" << endl;
    cout << "MAC: " << nuevo.mac << endl;
    cout << "IP: " << nuevo.ip << endl;
    cout << "Nombre: " << nuevo.nombre << endl;
    cout << "Autorizado: " << (nuevo.autorizado ? "Si" : "No") << endl;
}

// Función 2: Validar Acceso
void validarAcceso() {
    cout << "\n========================================" << endl;
    cout << "         VALIDAR ACCESO A RED" << endl;
    cout << "========================================" << endl;
    
    string mac;
    cout << "Ingrese la direccion MAC del dispositivo: ";
    getline(cin, mac);
    
    // Buscar dispositivo
    bool encontrado = false;
    for (auto& dispositivo : dispositivos) {
        if (dispositivo.mac == mac) {
            encontrado = true;
            
            // Verificar si ya está conectado
            if (dispositivo.conectado) {
                cout << "\n⚠ ADVERTENCIA: Este dispositivo ya esta conectado." << endl;
                return;
            }
            
            // Verificar autorización
            if (!dispositivo.autorizado) {
                // Generar alerta de acceso no autorizado
                Alerta alerta;
                alerta.tipo = "ACCESO NO AUTORIZADO";
                alerta.mensaje = "Intento de conexion de dispositivo no autorizado";
                alerta.dispositivo = dispositivo.mac + " (" + dispositivo.nombre + ")";
                alerta.hora = obtenerHoraActual();
                alertas.push_back(alerta);
                
                cout << "\n✗ ACCESO DENEGADO: Dispositivo no autorizado." << endl;
                cout << "Se ha generado una alerta de seguridad." << endl;
                return;
            }
            
            // Verificar límite de conexiones simultáneas
            int conexionesActivas = contarConexionesActivas();
            if (conexionesActivas >= MAX_CONEXIONES_SIMULTANEAS) {
                // Generar alerta de límite excedido
                Alerta alerta;
                alerta.tipo = "LIMITE EXCEDIDO";
                alerta.mensaje = "Se intento conectar pero se alcanzo el limite de conexiones";
                alerta.dispositivo = dispositivo.mac + " (" + dispositivo.nombre + ")";
                alerta.hora = obtenerHoraActual();
                alertas.push_back(alerta);
                
                cout << "\n✗ ACCESO DENEGADO: Limite de conexiones simultaneas alcanzado." << endl;
                cout << "Conexiones activas: " << conexionesActivas << "/" << MAX_CONEXIONES_SIMULTANEAS << endl;
                cout << "Se ha generado una alerta." << endl;
                return;
            }
            
            // Permitir conexión
            dispositivo.conectado = true;
            time_t ahora = time(0);
            tm* tiempo = localtime(&ahora);
            dispositivo.horaConexion = tiempo->tm_hour;
            dispositivo.minutoConexion = tiempo->tm_min;
            
            cout << "\n✓ ACCESO PERMITIDO: Dispositivo conectado exitosamente." << endl;
            cout << "MAC: " << dispositivo.mac << endl;
            cout << "IP: " << dispositivo.ip << endl;
            cout << "Nombre: " << dispositivo.nombre << endl;
            cout << "Hora de conexion: " << obtenerHoraActual() << endl;
            cout << "Conexiones activas: " << (conexionesActivas + 1) << "/" << MAX_CONEXIONES_SIMULTANEAS << endl;
            
            return;
        }
    }
    
    if (!encontrado) {
        // Generar alerta de dispositivo no registrado
        Alerta alerta;
        alerta.tipo = "DISPOSITIVO NO REGISTRADO";
        alerta.mensaje = "Intento de conexion de dispositivo desconocido";
        alerta.dispositivo = mac;
        alerta.hora = obtenerHoraActual();
        alertas.push_back(alerta);
        
        cout << "\n✗ ACCESO DENEGADO: Dispositivo no registrado en el sistema." << endl;
        cout << "Se ha generado una alerta de seguridad." << endl;
    }
}

// Función 3: Generar Alertas
void generarAlertas() {
    cout << "\n========================================" << endl;
    cout << "        GENERAR REPORTE DE ALERTAS" << endl;
    cout << "========================================" << endl;
    
    // Verificar dispositivos no autorizados conectados
    for (const auto& dispositivo : dispositivos) {
        if (dispositivo.conectado && !dispositivo.autorizado) {
            bool alertaExiste = false;
            for (const auto& alerta : alertas) {
                if (alerta.dispositivo.find(dispositivo.mac) != string::npos && 
                    alerta.tipo == "DISPOSITIVO NO AUTORIZADO CONECTADO") {
                    alertaExiste = true;
                    break;
                }
            }
            
            if (!alertaExiste) {
                Alerta alerta;
                alerta.tipo = "DISPOSITIVO NO AUTORIZADO CONECTADO";
                alerta.mensaje = "Dispositivo no autorizado detectado en la red";
                alerta.dispositivo = dispositivo.mac + " (" + dispositivo.nombre + ")";
                alerta.hora = obtenerHoraActual();
                alertas.push_back(alerta);
            }
        }
    }
    
    // Verificar si se está cerca del límite de conexiones
    int conexionesActivas = contarConexionesActivas();
    if (conexionesActivas >= (MAX_CONEXIONES_SIMULTANEAS * 0.8)) {
        bool alertaExiste = false;
        for (const auto& alerta : alertas) {
            if (alerta.tipo == "ADVERTENCIA: Cerca del limite") {
                alertaExiste = true;
                break;
            }
        }
        
        if (!alertaExiste && conexionesActivas < MAX_CONEXIONES_SIMULTANEAS) {
            Alerta alerta;
            alerta.tipo = "ADVERTENCIA: Cerca del limite";
            alerta.mensaje = "Se esta cerca del limite de conexiones simultaneas";
            alerta.dispositivo = "Sistema";
            alerta.hora = obtenerHoraActual();
            alertas.push_back(alerta);
        }
    }
    
    cout << "✓ Proceso de generacion de alertas completado." << endl;
    cout << "Total de alertas en el sistema: " << alertas.size() << endl;
}

// Función para mostrar dispositivos registrados
void mostrarDispositivos() {
    cout << "\n========================================" << endl;
    cout << "    DISPOSITIVOS REGISTRADOS" << endl;
    cout << "========================================" << endl;
    
    if (dispositivos.empty()) {
        cout << "No hay dispositivos registrados." << endl;
        return;
    }
    
    cout << left << setw(20) << "MAC" 
         << setw(18) << "IP" 
         << setw(25) << "Nombre" 
         << setw(12) << "Autorizado" 
         << setw(12) << "Estado" << endl;
    cout << "----------------------------------------------------------------------------" << endl;
    
    for (const auto& dispositivo : dispositivos) {
        cout << left << setw(20) << dispositivo.mac
             << setw(18) << dispositivo.ip
             << setw(25) << dispositivo.nombre
             << setw(12) << (dispositivo.autorizado ? "Si" : "No")
             << setw(12) << (dispositivo.conectado ? "Conectado" : "Desconectado") << endl;
    }
    
    cout << "\nTotal de dispositivos: " << dispositivos.size() << endl;
}

// Función para mostrar conexiones activas
void mostrarConexionesActivas() {
    cout << "\n========================================" << endl;
    cout << "       CONEXIONES ACTIVAS" << endl;
    cout << "========================================" << endl;
    
    int conexionesActivas = contarConexionesActivas();
    
    if (conexionesActivas == 0) {
        cout << "No hay conexiones activas en este momento." << endl;
        return;
    }
    
    cout << left << setw(20) << "MAC" 
         << setw(18) << "IP" 
         << setw(25) << "Nombre" 
         << setw(15) << "Hora Conexion" << endl;
    cout << "----------------------------------------------------------------------------" << endl;
    
    for (const auto& dispositivo : dispositivos) {
        if (dispositivo.conectado) {
            string horaConexion = to_string(dispositivo.horaConexion) + ":" + 
                                 (dispositivo.minutoConexion < 10 ? "0" : "") + 
                                 to_string(dispositivo.minutoConexion);
            
            cout << left << setw(20) << dispositivo.mac
                 << setw(18) << dispositivo.ip
                 << setw(25) << dispositivo.nombre
                 << setw(15) << horaConexion << endl;
        }
    }
    
    cout << "\nConexiones activas: " << conexionesActivas << "/" << MAX_CONEXIONES_SIMULTANEAS << endl;
}

// Función para mostrar alertas
void mostrarAlertas() {
    cout << "\n========================================" << endl;
    cout << "           ALERTAS DEL SISTEMA" << endl;
    cout << "========================================" << endl;
    
    if (alertas.empty()) {
        cout << "No hay alertas registradas." << endl;
        return;
    }
    
    cout << left << setw(30) << "Tipo" 
         << setw(40) << "Mensaje" 
         << setw(30) << "Dispositivo" 
         << setw(10) << "Hora" << endl;
    cout << "--------------------------------------------------------------------------------------------------------" << endl;
    
    for (const auto& alerta : alertas) {
        cout << left << setw(30) << alerta.tipo
             << setw(40) << alerta.mensaje
             << setw(30) << alerta.dispositivo
             << setw(10) << alerta.hora << endl;
    }
    
    cout << "\nTotal de alertas: " << alertas.size() << endl;
}

// Función para desconectar un dispositivo
void desconectarDispositivo() {
    cout << "\n========================================" << endl;
    cout << "      DESCONECTAR DISPOSITIVO" << endl;
    cout << "========================================" << endl;
    
    string mac;
    cout << "Ingrese la direccion MAC del dispositivo a desconectar: ";
    getline(cin, mac);
    
    for (auto& dispositivo : dispositivos) {
        if (dispositivo.mac == mac) {
            if (dispositivo.conectado) {
                dispositivo.conectado = false;
                cout << "\n✓ Dispositivo desconectado exitosamente." << endl;
                cout << "MAC: " << dispositivo.mac << endl;
                cout << "Nombre: " << dispositivo.nombre << endl;
            } else {
                cout << "\n⚠ El dispositivo no esta conectado." << endl;
            }
            return;
        }
    }
    
    cout << "\n✗ Dispositivo no encontrado." << endl;
}

