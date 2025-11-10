"""
Sistema de Control de Accesos a Red WiFi
Objetivo: Registrar dispositivos por MAC e IP, controlar límite de conexiones 
simultáneas y generar alertas por accesos no autorizados.
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from datetime import datetime
import re
from collections import defaultdict

class ControlWiFi:
    """Clase principal para gestionar el control de accesos WiFi"""
    
    def __init__(self):
        # Vectores: lista de dispositivos registrados
        self.dispositivos = []  # Lista de diccionarios con info de dispositivos
        
        # Matrices: conexiones por usuario [usuario][dispositivo] = estado
        self.conexiones = defaultdict(list)
        
        # Parámetros de control
        self.limite_conexiones = 5  # Límite de conexiones simultáneas
        self.conexiones_activas = 0
        
        # Historial de alertas
        self.alertas = []
        
        # Dispositivos bloqueados
        self.dispositivos_bloqueados = set()
        
        # Dispositivos autorizados por defecto
        self.dispositivos_autorizados = set()

    def registrar_dispositivo(self, nombre, mac, ip, usuario, estado="Activo"):
        """
        Función: Registrar un dispositivo en la red
        Valida el formato de MAC e IP antes de registrar
        """
        # Validación de MAC
        if not self._validar_mac(mac):
            return False, "Formato de MAC inválido. Use: XX:XX:XX:XX:XX:XX"
        
        # Validación de IP
        if not self._validar_ip(ip):
            return False, "Formato de IP inválido. Use: XXX.XXX.XXX.XXX"
        
        # Verificar duplicados
        for device in self.dispositivos:
            if device['mac'] == mac:
                return False, f"Dispositivo con MAC {mac} ya existe"
        
        # Registrar dispositivo
        dispositivo = {
            'id': len(self.dispositivos) + 1,
            'nombre': nombre,
            'mac': mac,
            'ip': ip,
            'usuario': usuario,
            'estado': estado,
            'fecha_registro': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'intentos_acceso': 0
        }
        
        self.dispositivos.append(dispositivo)
        self.dispositivos_autorizados.add(mac)
        
        # Generar alerta de nuevo registro
        self._generar_alerta(f"✓ Dispositivo '{nombre}' registrado exitosamente", "INFO")
        
        return True, "Dispositivo registrado correctamente"

    def validar_acceso(self, mac, ip):
        """
        Función: Validar si un dispositivo puede acceder a la red
        Controla: límite de conexiones, MAC bloqueadas, IPs no autorizadas
        """
        # Condicional: verificar si está bloqueado
        if mac in self.dispositivos_bloqueados:
            self._generar_alerta(f"⛔ ACCESO DENEGADO: MAC {mac} está bloqueada", "CRITICA")
            return False, "Dispositivo bloqueado"
        
        # Condicional: verificar si es autorizado
        if mac not in self.dispositivos_autorizados:
            self._generar_alerta(f"⚠️ ACCESO NO AUTORIZADO: MAC {mac} intenta conectarse", "ADVERTENCIA")
            return False, "Dispositivo no autorizado"
        
        # Bucle: verificar límite de conexiones
        if self.conexiones_activas >= self.limite_conexiones:
            self._generar_alerta(
                f"🚫 LÍMITE ALCANZADO: Máximo {self.limite_conexiones} conexiones simultáneas", 
                "ADVERTENCIA"
            )
            return False, "Límite de conexiones alcanzado"
        
        # Registrar conexión
        self.conexiones_activas += 1
        
        # Buscar dispositivo para actualizar
        for device in self.dispositivos:
            if device['mac'] == mac:
                device['intentos_acceso'] += 1
                self._generar_alerta(
                    f"✓ ACCESO PERMITIDO: {device['nombre']} ({mac}) conectado", 
                    "EXITO"
                )
                return True, f"Acceso permitido. Conexiones activas: {self.conexiones_activas}/{self.limite_conexiones}"
        
        return True, f"Acceso permitido. Conexiones activas: {self.conexiones_activas}/{self.limite_conexiones}"

    def desconectar_dispositivo(self, mac):
        """Desconectar un dispositivo y liberar conexión"""
        if self.conexiones_activas > 0:
            self.conexiones_activas -= 1
        
        for device in self.dispositivos:
            if device['mac'] == mac:
                self._generar_alerta(
                    f"→ Dispositivo '{device['nombre']}' desconectado", 
                    "INFO"
                )
                return True
        
        return False

    def bloquear_dispositivo(self, mac, razon="No especificada"):
        """Bloquear un dispositivo de la red"""
        if mac in self.dispositivos_bloqueados:
            return False, "Dispositivo ya está bloqueado"
        
        self.dispositivos_bloqueados.add(mac)
        self._generar_alerta(f"⛔ Dispositivo {mac} bloqueado. Razón: {razon}", "CRITICA")
        
        return True, "Dispositivo bloqueado correctamente"

    def desbloquear_dispositivo(self, mac):
        """Desbloquear un dispositivo"""
        if mac not in self.dispositivos_bloqueados:
            return False, "Dispositivo no está bloqueado"
        
        self.dispositivos_bloqueados.discard(mac)
        self._generar_alerta(f"✓ Dispositivo {mac} desbloqueado", "INFO")
        
        return True, "Dispositivo desbloqueado"

    def _generar_alerta(self, mensaje, tipo="INFO"):
        """
        Función: Generar alertas por accesos no autorizados
        Tipos: INFO, EXITO, ADVERTENCIA, CRITICA
        """
        timestamp = datetime.now().strftime("%H:%M:%S")
        alerta = {
            'timestamp': timestamp,
            'tipo': tipo,
            'mensaje': mensaje
        }
        self.alertas.append(alerta)

    def _validar_mac(self, mac):
        """Validar formato de dirección MAC"""
        patron = r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'
        return bool(re.match(patron, mac))

    def _validar_ip(self, ip):
        """Validar formato de dirección IP"""
        patron = r'^(\d{1,3}\.){3}\d{1,3}$'
        if not re.match(patron, ip):
            return False
        
        partes = ip.split('.')
        for parte in partes:
            if not 0 <= int(parte) <= 255:
                return False
        
        return True

    def obtener_dispositivos(self):
        """Retorna lista de dispositivos registrados"""
        return self.dispositivos

    def obtener_alertas(self):
        """Retorna historial de alertas"""
        return self.alertas

    def obtener_estadisticas(self):
        """Retorna estadísticas del sistema"""
        return {
            'total_dispositivos': len(self.dispositivos),
            'conexiones_activas': self.conexiones_activas,
            'limite_conexiones': self.limite_conexiones,
            'dispositivos_bloqueados': len(self.dispositivos_bloqueados),
            'total_alertas': len(self.alertas)
        }


class InterfazWiFi:
    """Interfaz gráfica para el sistema de control WiFi"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Control de Accesos a Red WiFi")
        self.root.geometry("1200x700")
        self.root.configure(bg="#f0f0f0")
        
        # Instancia del sistema de control
        self.control = ControlWiFi()
        
        # Colores para la interfaz
        self.color_primario = "#2c3e50"
        self.color_secundario = "#3498db"
        self.color_exito = "#27ae60"
        self.color_error = "#e74c3c"
        self.color_advertencia = "#f39c12"
        
        self._crear_interfaz()
        self._cargar_datos_ejemplo()

    def _crear_interfaz(self):
        """Crear la interfaz gráfica principal"""
        # Barra de título
        titulo = tk.Label(
            self.root, 
            text="🔒 Sistema de Control de Accesos a Red WiFi",
            font=("Arial", 16, "bold"),
            bg=self.color_primario,
            fg="white",
            pady=10
        )
        titulo.pack(fill="x")
        
        # Frame principal con tabs
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Tab 1: Registro de Dispositivos
        self.tab_registro = ttk.Frame(notebook)
        notebook.add(self.tab_registro, text="📝 Registrar Dispositivo")
        self._crear_tab_registro()
        
        # Tab 2: Validar Acceso
        self.tab_acceso = ttk.Frame(notebook)
        notebook.add(self.tab_acceso, text="🔐 Validar Acceso")
        self._crear_tab_acceso()
        
        # Tab 3: Gestión de Dispositivos
        self.tab_dispositivos = ttk.Frame(notebook)
        notebook.add(self.tab_dispositivos, text="📱 Dispositivos Registrados")
        self._crear_tab_dispositivos()
        
        # Tab 4: Alertas y Estadísticas
        self.tab_alertas = ttk.Frame(notebook)
        notebook.add(self.tab_alertas, text="⚠️ Alertas y Estadísticas")
        self._crear_tab_alertas()

    def _crear_tab_registro(self):
        """Tab para registrar nuevos dispositivos"""
        frame_principal = ttk.Frame(self.tab_registro, padding="20")
        frame_principal.pack(fill="both", expand=True)
        
        # Título
        titulo = ttk.Label(frame_principal, text="Registrar Nuevo Dispositivo", 
                          font=("Arial", 12, "bold"))
        titulo.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Campos de entrada
        campos = [
            ("Nombre del Dispositivo:", "nombre"),
            ("Dirección MAC (XX:XX:XX:XX:XX:XX):", "mac"),
            ("Dirección IP (XXX.XXX.XXX.XXX):", "ip"),
            ("Usuario/Propietario:", "usuario"),
        ]
        
        self.entradas_registro = {}
        for i, (label, key) in enumerate(campos, start=1):
            ttk.Label(frame_principal, text=label).grid(row=i, column=0, sticky="w", pady=5)
            entrada = ttk.Entry(frame_principal, width=40)
            entrada.grid(row=i, column=1, pady=5, padx=10)
            self.entradas_registro[key] = entrada
        
        # Botón registrar
        btn_registrar = ttk.Button(
            frame_principal,
            text="✅ Registrar Dispositivo",
            command=self._registrar_dispositivo
        )
        btn_registrar.grid(row=len(campos)+1, column=0, columnspan=2, pady=20)
        
        # Label de estado
        self.label_status_registro = ttk.Label(
            frame_principal, 
            text="",
            foreground="green"
        )
        self.label_status_registro.grid(row=len(campos)+2, column=0, columnspan=2)

    def _crear_tab_acceso(self):
        """Tab para validar acceso de dispositivos"""
        frame_principal = ttk.Frame(self.tab_acceso, padding="20")
        frame_principal.pack(fill="both", expand=True)
        
        # Título
        titulo = ttk.Label(frame_principal, text="Validar Acceso a la Red", 
                          font=("Arial", 12, "bold"))
        titulo.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Selector de dispositivo
        ttk.Label(frame_principal, text="Seleccionar Dispositivo:").grid(row=1, column=0, sticky="w", pady=5)
        self.combo_dispositivos = ttk.Combobox(
            frame_principal, 
            width=40, 
            state="readonly"
        )
        self.combo_dispositivos.grid(row=1, column=1, pady=5, padx=10)
        
        # Botones de control
        frame_botones = ttk.Frame(frame_principal)
        frame_botones.grid(row=2, column=0, columnspan=2, pady=20)
        
        ttk.Button(
            frame_botones,
            text="✅ Conectar",
            command=self._conectar_dispositivo
        ).pack(side="left", padx=5)
        
        ttk.Button(
            frame_botones,
            text="❌ Desconectar",
            command=self._desconectar_dispositivo
        ).pack(side="left", padx=5)
        
        ttk.Button(
            frame_botones,
            text="🚫 Bloquear",
            command=self._bloquear_dispositivo_dialog
        ).pack(side="left", padx=5)
        
        ttk.Button(
            frame_botones,
            text="🔓 Desbloquear",
            command=self._desbloquear_dispositivo
        ).pack(side="left", padx=5)
        
        # Label de estado
        self.label_status_acceso = ttk.Label(
            frame_principal, 
            text="",
            foreground="green"
        )
        self.label_status_acceso.grid(row=3, column=0, columnspan=2)
        
        # Información de conexiones
        frame_info = ttk.LabelFrame(frame_principal, text="Estado de Conexiones", padding="10")
        frame_info.grid(row=4, column=0, columnspan=2, pady=20, sticky="nsew")
        
        self.label_conexiones = ttk.Label(
            frame_info, 
            text="Conexiones activas: 0/5",
            font=("Arial", 11, "bold")
        )
        self.label_conexiones.pack()

    def _crear_tab_dispositivos(self):
        """Tab para ver dispositivos registrados"""
        frame_principal = ttk.Frame(self.tab_dispositivos, padding="10")
        frame_principal.pack(fill="both", expand=True)
        
        # Tabla de dispositivos
        self.tree_dispositivos = ttk.Treeview(
            frame_principal,
            columns=("ID", "Nombre", "MAC", "IP", "Usuario", "Estado", "Intentos", "Fecha"),
            height=15
        )
        
        # Definir columnas
        self.tree_dispositivos.column("#0", width=0, stretch=False)
        columnas_ancho = {
            "ID": 40,
            "Nombre": 120,
            "MAC": 150,
            "IP": 120,
            "Usuario": 100,
            "Estado": 80,
            "Intentos": 70,
            "Fecha": 150
        }
        
        for col, ancho in columnas_ancho.items():
            self.tree_dispositivos.column(col, anchor="w", width=ancho)
            self.tree_dispositivos.heading(col, text=col)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(frame_principal, orient="vertical", command=self.tree_dispositivos.yview)
        self.tree_dispositivos.configure(yscroll=scrollbar.set)
        
        self.tree_dispositivos.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Botón actualizar
        ttk.Button(
            frame_principal,
            text="🔄 Actualizar Lista",
            command=self._actualizar_tabla_dispositivos
        ).pack(pady=10)

    def _crear_tab_alertas(self):
        """Tab para ver alertas y estadísticas"""
        frame_principal = ttk.Frame(self.tab_alertas, padding="10")
        frame_principal.pack(fill="both", expand=True)
        
        # Frame de estadísticas
        frame_stats = ttk.LabelFrame(frame_principal, text="📊 Estadísticas del Sistema", padding="10")
        frame_stats.pack(fill="x", pady=10)
        
        self.label_stats = ttk.Label(frame_stats, text="", font=("Arial", 10))
        self.label_stats.pack(fill="x")
        
        # Historial de alertas
        frame_alertas = ttk.LabelFrame(frame_principal, text="⚠️ Historial de Alertas", padding="10")
        frame_alertas.pack(fill="both", expand=True, pady=10)
        
        # Text widget para alertas
        self.text_alertas = scrolledtext.ScrolledText(
            frame_alertas,
            height=15,
            width=100,
            font=("Courier", 9)
        )
        self.text_alertas.pack(fill="both", expand=True)
        
        # Configurar tags de colores para alertas
        self.text_alertas.tag_configure("INFO", foreground="#2c3e50")
        self.text_alertas.tag_configure("EXITO", foreground="#27ae60")
        self.text_alertas.tag_configure("ADVERTENCIA", foreground="#f39c12")
        self.text_alertas.tag_configure("CRITICA", foreground="#e74c3c", background="#fadbd8")
        
        # Botones de control
        frame_botones = ttk.Frame(frame_principal)
        frame_botones.pack(fill="x", pady=10)
        
        ttk.Button(
            frame_botones,
            text="🔄 Actualizar Alertas",
            command=self._actualizar_alertas
        ).pack(side="left", padx=5)
        
        ttk.Button(
            frame_botones,
            text="🗑️ Limpiar Alertas",
            command=self._limpiar_alertas
        ).pack(side="left", padx=5)

    def _registrar_dispositivo(self):
        """Registrar un nuevo dispositivo"""
        try:
            nombre = self.entradas_registro['nombre'].get().strip()
            mac = self.entradas_registro['mac'].get().strip()
            ip = self.entradas_registro['ip'].get().strip()
            usuario = self.entradas_registro['usuario'].get().strip()
            
            if not all([nombre, mac, ip, usuario]):
                messagebox.showerror("Error", "Todos los campos son requeridos")
                return
            
            exito, mensaje = self.control.registrar_dispositivo(nombre, mac, ip, usuario)
            
            if exito:
                self.label_status_registro.config(text=mensaje, foreground="green")
                # Limpiar campos
                for entrada in self.entradas_registro.values():
                    entrada.delete(0, "end")
                self._actualizar_combo_dispositivos()
                self._actualizar_tabla_dispositivos()
                messagebox.showinfo("Éxito", mensaje)
            else:
                self.label_status_registro.config(text=mensaje, foreground="red")
                messagebox.showerror("Error", mensaje)
        
        except Exception as e:
            messagebox.showerror("Error", f"Error al registrar: {str(e)}")

    def _conectar_dispositivo(self):
        """Conectar un dispositivo a la red"""
        mac_seleccionada = self.combo_dispositivos.get()
        
        if not mac_seleccionada:
            messagebox.showwarning("Advertencia", "Seleccione un dispositivo")
            return
        
        # Extraer MAC de la selección (formato: "Nombre (MAC)")
        mac = mac_seleccionada.split("(")[-1].rstrip(")")
        
        exito, mensaje = self.control.validar_acceso(mac, "")
        
        self.label_status_acceso.config(
            text=mensaje,
            foreground="green" if exito else "red"
        )
        self._actualizar_alertas()
        self._actualizar_estadisticas()
        self.label_conexiones.config(
            text=f"Conexiones activas: {self.control.conexiones_activas}/{self.control.limite_conexiones}"
        )

    def _desconectar_dispositivo(self):
        """Desconectar un dispositivo"""
        mac_seleccionada = self.combo_dispositivos.get()
        
        if not mac_seleccionada:
            messagebox.showwarning("Advertencia", "Seleccione un dispositivo")
            return
        
        mac = mac_seleccionada.split("(")[-1].rstrip(")")
        self.control.desconectar_dispositivo(mac)
        
        self.label_status_acceso.config(
            text="Dispositivo desconectado",
            foreground="blue"
        )
        self._actualizar_alertas()
        self._actualizar_estadisticas()
        self.label_conexiones.config(
            text=f"Conexiones activas: {self.control.conexiones_activas}/{self.control.limite_conexiones}"
        )

    def _bloquear_dispositivo_dialog(self):
        """Abrir diálogo para bloquear dispositivo"""
        mac_seleccionada = self.combo_dispositivos.get()
        
        if not mac_seleccionada:
            messagebox.showwarning("Advertencia", "Seleccione un dispositivo")
            return
        
        # Crear ventana de diálogo
        dialog = tk.Toplevel(self.root)
        dialog.title("Bloquear Dispositivo")
        dialog.geometry("400x150")
        
        ttk.Label(dialog, text="Razón del bloqueo:").pack(pady=10)
        entrada_razon = ttk.Entry(dialog, width=40)
        entrada_razon.pack(pady=5)
        
        def bloquear():
            mac = mac_seleccionada.split("(")[-1].rstrip(")")
            razon = entrada_razon.get().strip()
            if not razon:
                razon = "No especificada"
            
            self.control.bloquear_dispositivo(mac, razon)
            self._actualizar_alertas()
            messagebox.showinfo("Éxito", "Dispositivo bloqueado")
            dialog.destroy()
        
        ttk.Button(dialog, text="Bloquear", command=bloquear).pack(pady=10)

    def _desbloquear_dispositivo(self):
        """Desbloquear un dispositivo"""
        mac_seleccionada = self.combo_dispositivos.get()
        
        if not mac_seleccionada:
            messagebox.showwarning("Advertencia", "Seleccione un dispositivo")
            return
        
        mac = mac_seleccionada.split("(")[-1].rstrip(")")
        exito, mensaje = self.control.desbloquear_dispositivo(mac)
        
        if exito:
            self._actualizar_alertas()
            messagebox.showinfo("Éxito", mensaje)
        else:
            messagebox.showwarning("Advertencia", mensaje)

    def _actualizar_combo_dispositivos(self):
        """Actualizar combo box de dispositivos"""
        dispositivos = self.control.obtener_dispositivos()
        opciones = [f"{d['nombre']} ({d['mac']})" for d in dispositivos]
        self.combo_dispositivos['values'] = opciones

    def _actualizar_tabla_dispositivos(self):
        """Actualizar tabla de dispositivos"""
        # Limpiar tabla
        for item in self.tree_dispositivos.get_children():
            self.tree_dispositivos.delete(item)
        
        # Llenar tabla
        dispositivos = self.control.obtener_dispositivos()
        for device in dispositivos:
            estado = "🚫 Bloqueado" if device['mac'] in self.control.dispositivos_bloqueados else "✅ Activo"
            self.tree_dispositivos.insert("", "end", values=(
                device['id'],
                device['nombre'],
                device['mac'],
                device['ip'],
                device['usuario'],
                estado,
                device['intentos_acceso'],
                device['fecha_registro']
            ))

    def _actualizar_alertas(self):
        """Actualizar historial de alertas"""
        self.text_alertas.config(state="normal")
        self.text_alertas.delete("1.0", "end")
        
        alertas = self.control.obtener_alertas()
        for alerta in alertas[-50:]:  # Mostrar últimas 50 alertas
            texto = f"[{alerta['timestamp']}] {alerta['mensaje']}\n"
            self.text_alertas.insert("end", texto, alerta['tipo'])
        
        self.text_alertas.see("end")
        self.text_alertas.config(state="disabled")

    def _actualizar_estadisticas(self):
        """Actualizar estadísticas del sistema"""
        stats = self.control.obtener_estadisticas()
        texto = (
            f"Total de dispositivos registrados: {stats['total_dispositivos']} | "
            f"Conexiones activas: {stats['conexiones_activas']}/{stats['limite_conexiones']} | "
            f"Dispositivos bloqueados: {stats['dispositivos_bloqueados']} | "
            f"Total de alertas: {stats['total_alertas']}"
        )
        self.label_stats.config(text=texto)

    def _limpiar_alertas(self):
        """Limpiar historial de alertas"""
        if messagebox.askyesno("Confirmar", "¿Desea limpiar el historial de alertas?"):
            self.control.alertas.clear()
            self._actualizar_alertas()
            messagebox.showinfo("Éxito", "Historial de alertas limpiado")

    def _cargar_datos_ejemplo(self):
        """Cargar datos de ejemplo para demostración"""
        # Registrar algunos dispositivos de ejemplo
        dispositivos_ejemplo = [
            ("Laptop Juan", "00:1A:2B:3C:4D:5E", "192.168.1.100", "juan.perez"),
            ("iPhone María", "00:1F:3B:4C:5D:6E", "192.168.1.101", "maria.garcia"),
            ("Tablet Carlos", "00:2A:3B:4C:5D:6F", "192.168.1.102", "carlos.lopez"),
            ("Smart TV", "00:3A:3B:4C:5D:70", "192.168.1.103", "admin"),
        ]
        
        for nombre, mac, ip, usuario in dispositivos_ejemplo:
            self.control.registrar_dispositivo(nombre, mac, ip, usuario)
        
        self._actualizar_combo_dispositivos()
        self._actualizar_tabla_dispositivos()
        self._actualizar_alertas()
        self._actualizar_estadisticas()


def main():
    """Función principal"""
    root = tk.Tk()
    app = InterfazWiFi(root)
    root.mainloop()


if __name__ == "__main__":
    main()
