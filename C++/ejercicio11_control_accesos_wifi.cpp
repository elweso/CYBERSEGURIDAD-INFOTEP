#include <windows.h>
#include <commctrl.h>
#include <string>
#include <vector>
#include <sstream>
#include <iomanip>
#include <ctime>
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

// IDs de controles
#define ID_BTN_REGISTRAR 1001
#define ID_BTN_VALIDAR 1002
#define ID_BTN_ALERTAS 1003
#define ID_BTN_DESCONECTAR 1004
#define ID_BTN_SALIR 1005
#define ID_EDIT_MAC 2001
#define ID_EDIT_IP 2002
#define ID_EDIT_NOMBRE 2003
#define ID_CHECK_AUTORIZADO 2004
#define ID_LIST_DISPOSITIVOS 3001
#define ID_LIST_ALERTAS 3002
#define ID_STATIC_INFO 4001
#define ID_STATIC_CONEXIONES 4002
#define ID_EDIT_MAC_VALIDAR 2005

// Prototipos de funciones
LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam);
void RegistrarDispositivo(HWND hwnd);
void ValidarAcceso(HWND hwnd);
void GenerarAlertas(HWND hwnd);
void DesconectarDispositivo(HWND hwnd);
void ActualizarListaDispositivos(HWND hwnd);
void ActualizarListaAlertas(HWND hwnd);
void ActualizarInfo(HWND hwnd);
bool ValidarFormatoMAC(const string& mac);
bool ValidarFormatoIP(const string& ip);
bool DispositivoExiste(const string& mac);
int ContarConexionesActivas();
string ObtenerHoraActual();
string ObtenerTextoEdit(HWND hEdit);
void MostrarMensaje(HWND hwnd, const string& titulo, const string& mensaje, bool esError = false);

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow) {
    const char CLASS_NAME[] = "ControlAccesosWiFi";
    
    WNDCLASSA wc = {};
    wc.lpfnWndProc = WindowProc;
    wc.hInstance = hInstance;
    wc.lpszClassName = CLASS_NAME;
    wc.hbrBackground = (HBRUSH)(COLOR_WINDOW + 1);
    wc.hCursor = LoadCursor(NULL, IDC_ARROW);
    
    RegisterClassA(&wc);
    
    HWND hwnd = CreateWindowExA(
        0,
        CLASS_NAME,
        "Sistema de Control de Accesos WiFi",
        WS_OVERLAPPEDWINDOW & ~WS_THICKFRAME & ~WS_MAXIMIZEBOX,
        CW_USEDEFAULT, CW_USEDEFAULT, 1000, 700,
        NULL, NULL, hInstance, NULL
    );
    
    if (hwnd == NULL) {
        return 0;
    }
    
    ShowWindow(hwnd, nCmdShow);
    UpdateWindow(hwnd);
    
    MSG msg = {};
    while (GetMessage(&msg, NULL, 0, 0)) {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }
    
    return 0;
}

LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam) {
    switch (uMsg) {
        case WM_CREATE: {
            // Título
            CreateWindowA("STATIC", "SISTEMA DE CONTROL DE ACCESOS WiFi",
                WS_VISIBLE | WS_CHILD | SS_CENTER,
                10, 10, 980, 30, hwnd, NULL, NULL, NULL);
            
            // Información de conexiones
            CreateWindowA("STATIC", "Conexiones activas: 0/5",
                WS_VISIBLE | WS_CHILD | SS_LEFT,
                10, 45, 300, 20, hwnd, (HMENU)ID_STATIC_CONEXIONES, NULL, NULL);
            
            // Grupo: Registrar Dispositivo
            CreateWindowA("STATIC", "REGISTRAR DISPOSITIVO",
                WS_VISIBLE | WS_CHILD | SS_LEFT | SS_SUNKEN,
                10, 75, 480, 20, hwnd, NULL, NULL, NULL);
            
            CreateWindowA("STATIC", "MAC (XX:XX:XX:XX:XX:XX):",
                WS_VISIBLE | WS_CHILD | SS_LEFT,
                20, 105, 200, 20, hwnd, NULL, NULL, NULL);
            CreateWindowA("EDIT", "",
                WS_VISIBLE | WS_CHILD | WS_BORDER | ES_LEFT,
                20, 125, 250, 25, hwnd, (HMENU)ID_EDIT_MAC, NULL, NULL);
            
            CreateWindowA("STATIC", "IP (X.X.X.X):",
                WS_VISIBLE | WS_CHILD | SS_LEFT,
                20, 155, 200, 20, hwnd, NULL, NULL, NULL);
            CreateWindowA("EDIT", "",
                WS_VISIBLE | WS_CHILD | WS_BORDER | ES_LEFT,
                20, 175, 250, 25, hwnd, (HMENU)ID_EDIT_IP, NULL, NULL);
            
            CreateWindowA("STATIC", "Nombre:",
                WS_VISIBLE | WS_CHILD | SS_LEFT,
                20, 205, 200, 20, hwnd, NULL, NULL, NULL);
            CreateWindowA("EDIT", "",
                WS_VISIBLE | WS_CHILD | WS_BORDER | ES_LEFT,
                20, 225, 250, 25, hwnd, (HMENU)ID_EDIT_NOMBRE, NULL, NULL);
            
            CreateWindowA("BUTTON", "Autorizado",
                WS_VISIBLE | WS_CHILD | BS_AUTOCHECKBOX,
                20, 260, 150, 25, hwnd, (HMENU)ID_CHECK_AUTORIZADO, NULL, NULL);
            
            CreateWindowA("BUTTON", "Registrar Dispositivo",
                WS_VISIBLE | WS_CHILD | BS_PUSHBUTTON,
                20, 295, 200, 35, hwnd, (HMENU)ID_BTN_REGISTRAR, NULL, NULL);
            
            // Grupo: Validar Acceso
            CreateWindowA("STATIC", "VALIDAR ACCESO",
                WS_VISIBLE | WS_CHILD | SS_LEFT | SS_SUNKEN,
                10, 345, 480, 20, hwnd, NULL, NULL, NULL);
            
            CreateWindowA("STATIC", "MAC del dispositivo:",
                WS_VISIBLE | WS_CHILD | SS_LEFT,
                20, 375, 200, 20, hwnd, NULL, NULL, NULL);
            CreateWindowA("EDIT", "",
                WS_VISIBLE | WS_CHILD | WS_BORDER | ES_LEFT,
                20, 395, 250, 25, hwnd, (HMENU)ID_EDIT_MAC_VALIDAR, NULL, NULL);
            
            CreateWindowA("BUTTON", "Validar Acceso",
                WS_VISIBLE | WS_CHILD | BS_PUSHBUTTON,
                20, 430, 200, 35, hwnd, (HMENU)ID_BTN_VALIDAR, NULL, NULL);
            
            CreateWindowA("BUTTON", "Desconectar",
                WS_VISIBLE | WS_CHILD | BS_PUSHBUTTON,
                240, 430, 200, 35, hwnd, (HMENU)ID_BTN_DESCONECTAR, NULL, NULL);
            
            CreateWindowA("BUTTON", "Generar Alertas",
                WS_VISIBLE | WS_CHILD | BS_PUSHBUTTON,
                20, 475, 200, 35, hwnd, (HMENU)ID_BTN_ALERTAS, NULL, NULL);
            
            // Lista de dispositivos
            CreateWindowA("STATIC", "DISPOSITIVOS REGISTRADOS",
                WS_VISIBLE | WS_CHILD | SS_LEFT | SS_SUNKEN,
                500, 75, 480, 20, hwnd, NULL, NULL, NULL);
            
            HWND hListDispositivos = CreateWindowExA(
                WS_EX_CLIENTEDGE,
                "SysListView32", "",
                WS_VISIBLE | WS_CHILD | LVS_REPORT | LVS_SINGLESEL | WS_VSCROLL,
                500, 100, 480, 250, hwnd, (HMENU)ID_LIST_DISPOSITIVOS, NULL, NULL
            );
            
            // Configurar columnas de la lista de dispositivos
            LVCOLUMNA lvc = {};
            lvc.mask = LVCF_TEXT | LVCF_WIDTH | LVCF_SUBITEM;
            
            lvc.iSubItem = 0;
            lvc.pszText = (LPSTR)"MAC";
            lvc.cx = 150;
            ListView_InsertColumn(hListDispositivos, 0, &lvc);
            
            lvc.iSubItem = 1;
            lvc.pszText = (LPSTR)"IP";
            lvc.cx = 120;
            ListView_InsertColumn(hListDispositivos, 1, &lvc);
            
            lvc.iSubItem = 2;
            lvc.pszText = (LPSTR)"Nombre";
            lvc.cx = 120;
            ListView_InsertColumn(hListDispositivos, 2, &lvc);
            
            lvc.iSubItem = 3;
            lvc.pszText = (LPSTR)"Estado";
            lvc.cx = 80;
            ListView_InsertColumn(hListDispositivos, 3, &lvc);
            
            // Lista de alertas
            CreateWindowA("STATIC", "ALERTAS DEL SISTEMA",
                WS_VISIBLE | WS_CHILD | SS_LEFT | SS_SUNKEN,
                500, 360, 480, 20, hwnd, NULL, NULL, NULL);
            
            HWND hListAlertas = CreateWindowExA(
                WS_EX_CLIENTEDGE,
                "SysListView32", "",
                WS_VISIBLE | WS_CHILD | LVS_REPORT | LVS_SINGLESEL | WS_VSCROLL,
                500, 385, 480, 250, hwnd, (HMENU)ID_LIST_ALERTAS, NULL, NULL
            );
            
            // Configurar columnas de la lista de alertas
            lvc.iSubItem = 0;
            lvc.pszText = (LPSTR)"Tipo";
            lvc.cx = 180;
            ListView_InsertColumn(hListAlertas, 0, &lvc);
            
            lvc.iSubItem = 1;
            lvc.pszText = (LPSTR)"Mensaje";
            lvc.cx = 200;
            ListView_InsertColumn(hListAlertas, 1, &lvc);
            
            lvc.iSubItem = 2;
            lvc.pszText = (LPSTR)"Hora";
            lvc.cx = 80;
            ListView_InsertColumn(hListAlertas, 2, &lvc);
            
            // Botón salir
            CreateWindowA("BUTTON", "Salir",
                WS_VISIBLE | WS_CHILD | BS_PUSHBUTTON,
                850, 640, 100, 30, hwnd, (HMENU)ID_BTN_SALIR, NULL, NULL);
            
            // Área de información
            CreateWindowA("STATIC", "",
                WS_VISIBLE | WS_CHILD | SS_LEFT | WS_BORDER,
                10, 520, 480, 150, hwnd, (HMENU)ID_STATIC_INFO, NULL, NULL);
            
            ActualizarInfo(hwnd);
            break;
        }
        
        case WM_COMMAND: {
            switch (LOWORD(wParam)) {
                case ID_BTN_REGISTRAR:
                    RegistrarDispositivo(hwnd);
                    break;
                case ID_BTN_VALIDAR:
                    ValidarAcceso(hwnd);
                    break;
                case ID_BTN_ALERTAS:
                    GenerarAlertas(hwnd);
                    break;
                case ID_BTN_DESCONECTAR:
                    DesconectarDispositivo(hwnd);
                    break;
                case ID_BTN_SALIR:
                    PostQuitMessage(0);
                    break;
            }
            break;
        }
        
        case WM_DESTROY:
            PostQuitMessage(0);
            return 0;
    }
    
    return DefWindowProc(hwnd, uMsg, wParam, lParam);
}

string ObtenerTextoEdit(HWND hEdit) {
    int length = GetWindowTextLengthA(hEdit) + 1;
    char* buffer = new char[length];
    GetWindowTextA(hEdit, buffer, length);
    string str(buffer);
    delete[] buffer;
    return str;
}

void MostrarMensaje(HWND hwnd, const string& titulo, const string& mensaje, bool esError) {
    MessageBoxA(hwnd, mensaje.c_str(), titulo.c_str(), 
               esError ? MB_ICONERROR | MB_OK : MB_ICONINFORMATION | MB_OK);
}

bool ValidarFormatoMAC(const string& mac) {
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

bool ValidarFormatoIP(const string& ip) {
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

bool DispositivoExiste(const string& mac) {
    for (const auto& dispositivo : dispositivos) {
        if (dispositivo.mac == mac) return true;
    }
    return false;
}

int ContarConexionesActivas() {
    int contador = 0;
    for (const auto& dispositivo : dispositivos) {
        if (dispositivo.conectado) contador++;
    }
    return contador;
}

string ObtenerHoraActual() {
    time_t ahora = time(0);
    tm* tiempo = localtime(&ahora);
    stringstream ss;
    ss << setfill('0') << setw(2) << tiempo->tm_hour << ":"
       << setfill('0') << setw(2) << tiempo->tm_min;
    return ss.str();
}

void ActualizarListaDispositivos(HWND hwnd) {
    HWND hList = GetDlgItem(hwnd, ID_LIST_DISPOSITIVOS);
    ListView_DeleteAllItems(hList);
    
    for (size_t i = 0; i < dispositivos.size(); i++) {
        const auto& d = dispositivos[i];
        
        LVITEMA lvi = {};
        lvi.mask = LVIF_TEXT;
        lvi.iItem = i;
        lvi.iSubItem = 0;
        lvi.pszText = (LPSTR)d.mac.c_str();
        ListView_InsertItem(hList, &lvi);
        
        ListView_SetItemText(hList, i, 1, (LPSTR)d.ip.c_str());
        ListView_SetItemText(hList, i, 2, (LPSTR)d.nombre.c_str());
        
        string estado = d.conectado ? "Conectado" : "Desconectado";
        ListView_SetItemText(hList, i, 3, (LPSTR)estado.c_str());
    }
}

void ActualizarListaAlertas(HWND hwnd) {
    HWND hList = GetDlgItem(hwnd, ID_LIST_ALERTAS);
    ListView_DeleteAllItems(hList);
    
    for (size_t i = 0; i < alertas.size(); i++) {
        const auto& a = alertas[i];
        
        LVITEMA lvi = {};
        lvi.mask = LVIF_TEXT;
        lvi.iItem = i;
        lvi.iSubItem = 0;
        lvi.pszText = (LPSTR)a.tipo.c_str();
        ListView_InsertItem(hList, &lvi);
        
        ListView_SetItemText(hList, i, 1, (LPSTR)a.mensaje.c_str());
        ListView_SetItemText(hList, i, 2, (LPSTR)a.hora.c_str());
    }
}

void ActualizarInfo(HWND hwnd) {
    int conexiones = ContarConexionesActivas();
    stringstream ss;
    ss << "Conexiones activas: " << conexiones << "/" << MAX_CONEXIONES_SIMULTANEAS;
    
    SetWindowTextA(GetDlgItem(hwnd, ID_STATIC_CONEXIONES), ss.str().c_str());
    
    // Actualizar información detallada
    ss.str("");
    ss << "=== INFORMACION DEL SISTEMA ===\n\n";
    ss << "Dispositivos registrados: " << dispositivos.size() << "\n";
    ss << "Conexiones activas: " << conexiones << "\n";
    ss << "Alertas generadas: " << alertas.size() << "\n";
    ss << "Limite de conexiones: " << MAX_CONEXIONES_SIMULTANEAS;
    
    SetWindowTextA(GetDlgItem(hwnd, ID_STATIC_INFO), ss.str().c_str());
}

void RegistrarDispositivo(HWND hwnd) {
    HWND hEditMac = GetDlgItem(hwnd, ID_EDIT_MAC);
    HWND hEditIP = GetDlgItem(hwnd, ID_EDIT_IP);
    HWND hEditNombre = GetDlgItem(hwnd, ID_EDIT_NOMBRE);
    HWND hCheckAutorizado = GetDlgItem(hwnd, ID_CHECK_AUTORIZADO);
    
    string mac = ObtenerTextoEdit(hEditMac);
    string ip = ObtenerTextoEdit(hEditIP);
    string nombre = ObtenerTextoEdit(hEditNombre);
    bool autorizado = (SendMessage(hCheckAutorizado, BM_GETCHECK, 0, 0) == BST_CHECKED);
    
    if (mac.empty() || ip.empty() || nombre.empty()) {
        MostrarMensaje(hwnd, "Error", "Por favor complete todos los campos.", true);
        return;
    }
    
    if (!ValidarFormatoMAC(mac)) {
        MostrarMensaje(hwnd, "Error", "Formato de MAC invalido. Use XX:XX:XX:XX:XX:XX", true);
        return;
    }
    
    if (!ValidarFormatoIP(ip)) {
        MostrarMensaje(hwnd, "Error", "Formato de IP invalido. Use X.X.X.X", true);
        return;
    }
    
    if (DispositivoExiste(mac)) {
        MostrarMensaje(hwnd, "Error", "Este dispositivo ya esta registrado.", true);
        return;
    }
    
    if (dispositivos.size() >= MAX_DISPOSITIVOS) {
        MostrarMensaje(hwnd, "Error", "Se ha alcanzado el limite maximo de dispositivos.", true);
        return;
    }
    
    Dispositivo nuevo;
    nuevo.mac = mac;
    nuevo.ip = ip;
    nuevo.nombre = nombre;
    nuevo.autorizado = autorizado;
    nuevo.conectado = false;
    nuevo.horaConexion = 0;
    nuevo.minutoConexion = 0;
    
    dispositivos.push_back(nuevo);
    
    // Limpiar campos
    SetWindowTextA(hEditMac, "");
    SetWindowTextA(hEditIP, "");
    SetWindowTextA(hEditNombre, "");
    SendMessage(hCheckAutorizado, BM_SETCHECK, BST_UNCHECKED, 0);
    
    ActualizarListaDispositivos(hwnd);
    ActualizarInfo(hwnd);
    MostrarMensaje(hwnd, "Exito", "Dispositivo registrado exitosamente.", false);
}

void ValidarAcceso(HWND hwnd) {
    HWND hEditMac = GetDlgItem(hwnd, ID_EDIT_MAC_VALIDAR);
    string mac = ObtenerTextoEdit(hEditMac);
    
    if (mac.empty()) {
        MostrarMensaje(hwnd, "Error", "Ingrese la direccion MAC del dispositivo.", true);
        return;
    }
    
    if (!ValidarFormatoMAC(mac)) {
        MostrarMensaje(hwnd, "Error", "Formato de MAC invalido.", true);
        return;
    }
    
    bool encontrado = false;
    for (auto& dispositivo : dispositivos) {
        if (dispositivo.mac == mac) {
            encontrado = true;
            
            if (dispositivo.conectado) {
                MostrarMensaje(hwnd, "Advertencia", "Este dispositivo ya esta conectado.", true);
                return;
            }
            
            if (!dispositivo.autorizado) {
                Alerta alerta;
                alerta.tipo = "ACCESO NO AUTORIZADO";
                alerta.mensaje = "Intento de conexion de dispositivo no autorizado";
                alerta.dispositivo = dispositivo.mac + " (" + dispositivo.nombre + ")";
                alerta.hora = ObtenerHoraActual();
                alertas.push_back(alerta);
                
                ActualizarListaAlertas(hwnd);
                MostrarMensaje(hwnd, "Acceso Denegado", "Dispositivo no autorizado. Se ha generado una alerta.", true);
                return;
            }
            
            int conexionesActivas = ContarConexionesActivas();
            if (conexionesActivas >= MAX_CONEXIONES_SIMULTANEAS) {
                Alerta alerta;
                alerta.tipo = "LIMITE EXCEDIDO";
                alerta.mensaje = "Se intento conectar pero se alcanzo el limite";
                alerta.dispositivo = dispositivo.mac + " (" + dispositivo.nombre + ")";
                alerta.hora = ObtenerHoraActual();
                alertas.push_back(alerta);
                
                ActualizarListaAlertas(hwnd);
                MostrarMensaje(hwnd, "Acceso Denegado", 
                    "Limite de conexiones alcanzado. Conexiones activas: " + 
                    to_string(conexionesActivas) + "/" + to_string(MAX_CONEXIONES_SIMULTANEAS), true);
                return;
            }
            
            dispositivo.conectado = true;
            time_t ahora = time(0);
            tm* tiempo = localtime(&ahora);
            dispositivo.horaConexion = tiempo->tm_hour;
            dispositivo.minutoConexion = tiempo->tm_min;
            
            ActualizarListaDispositivos(hwnd);
            ActualizarInfo(hwnd);
            
            string mensaje = "Dispositivo conectado exitosamente.\n";
            mensaje += "MAC: " + dispositivo.mac + "\n";
            mensaje += "IP: " + dispositivo.ip + "\n";
            mensaje += "Nombre: " + dispositivo.nombre + "\n";
            mensaje += "Hora: " + ObtenerHoraActual();
            
            MostrarMensaje(hwnd, "Acceso Permitido", mensaje, false);
            return;
        }
    }
    
    if (!encontrado) {
        Alerta alerta;
        alerta.tipo = "DISPOSITIVO NO REGISTRADO";
        alerta.mensaje = "Intento de conexion de dispositivo desconocido";
        alerta.dispositivo = mac;
        alerta.hora = ObtenerHoraActual();
        alertas.push_back(alerta);
        
        ActualizarListaAlertas(hwnd);
        MostrarMensaje(hwnd, "Acceso Denegado", "Dispositivo no registrado. Se ha generado una alerta.", true);
    }
}

void GenerarAlertas(HWND hwnd) {
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
                alerta.hora = ObtenerHoraActual();
                alertas.push_back(alerta);
            }
        }
    }
    
    int conexionesActivas = ContarConexionesActivas();
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
            alerta.hora = ObtenerHoraActual();
            alertas.push_back(alerta);
        }
    }
    
    ActualizarListaAlertas(hwnd);
    ActualizarInfo(hwnd);
    MostrarMensaje(hwnd, "Exito", "Proceso de generacion de alertas completado.", false);
}

void DesconectarDispositivo(HWND hwnd) {
    HWND hList = GetDlgItem(hwnd, ID_LIST_DISPOSITIVOS);
    int seleccion = ListView_GetNextItem(hList, -1, LVNI_SELECTED);
    
    if (seleccion == -1) {
        MostrarMensaje(hwnd, "Error", "Seleccione un dispositivo de la lista.", true);
        return;
    }
    
    if (seleccion >= (int)dispositivos.size()) {
        return;
    }
    
    auto& dispositivo = dispositivos[seleccion];
    if (dispositivo.conectado) {
        dispositivo.conectado = false;
        ActualizarListaDispositivos(hwnd);
        ActualizarInfo(hwnd);
        MostrarMensaje(hwnd, "Exito", "Dispositivo desconectado exitosamente.", false);
    } else {
        MostrarMensaje(hwnd, "Advertencia", "El dispositivo no esta conectado.", true);
    }
}
