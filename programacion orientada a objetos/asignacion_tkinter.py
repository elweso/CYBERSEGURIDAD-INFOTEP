import tkinter as tk
from tkinter import messagebox

class Ejercicio1(tk.Toplevel):
    """
    1. Ventana básica con un mensaje de bienvenida.
    """
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Ejercicio 1: Bienvenida")
        self.geometry("300x100")
        
        # Label: Etiqueta de texto
        lbl_saludo = tk.Label(self, text="¡Bienvenido a Tkinter!", font=("Arial", 14, "bold"))
        lbl_saludo.pack(pady=30) # pady agrega espacio vertical


class Ejercicio2(tk.Toplevel):
    """
    2. Interfaz con Entry y Button. Muestra lo escrito en un Label.
    """
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Ejercicio 2: Eco de Texto")
        self.geometry("350x200")

        tk.Label(self, text="Escribe algo y presiona el botón:").pack(pady=10)

        # Entry: Campo de texto de una línea
        self.entrada = tk.Entry(self, width=30)
        self.entrada.pack(pady=5)

        # Button: Botón que ejecuta una función
        btn_mostrar = tk.Button(self, text="Mostrar Texto", command=self.mostrar_texto)
        btn_mostrar.pack(pady=10)

        # Label vacío donde aparecerá el resultado
        self.lbl_resultado = tk.Label(self, text="", fg="blue", font=("Arial", 12))
        self.lbl_resultado.pack(pady=10)

    def mostrar_texto(self):
        texto = self.entrada.get() # Obtener texto del Entry
        self.lbl_resultado.config(text=f"Escribiste: {texto}") # Actualizar Label


class Ejercicio3(tk.Toplevel):
    """
    3. Calculadora sencilla (Suma) usando Labels, Entries y Buttons.
    """
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Ejercicio 3: Sumadora")
        self.geometry("300x250")

        tk.Label(self, text="Número 1:").pack(pady=5)
        self.num1 = tk.Entry(self)
        self.num1.pack()

        tk.Label(self, text="Número 2:").pack(pady=5)
        self.num2 = tk.Entry(self)
        self.num2.pack()

        btn_sumar = tk.Button(self, text="Sumar", command=self.sumar, bg="lightgreen")
        btn_sumar.pack(pady=15)

        self.lbl_total = tk.Label(self, text="Resultado: 0", font=("Arial", 12, "bold"))
        self.lbl_total.pack()

    def sumar(self):
        try:
            # Convertir texto a flotante y sumar
            val1 = float(self.num1.get())
            val2 = float(self.num2.get())
            total = val1 + val2
            self.lbl_total.config(text=f"Resultado: {total}")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa solo números válidos.")


class Ejercicio4(tk.Toplevel):
    """
    4. Ventana con Listbox y botón para agregar elementos.
    """
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Ejercicio 4: Lista de Tareas")
        self.geometry("300x350")

        # Frame para organizar la entrada y el botón
        frame_entrada = tk.Frame(self)
        frame_entrada.pack(pady=10)

        self.entrada_item = tk.Entry(frame_entrada, width=20)
        self.entrada_item.pack(side=tk.LEFT, padx=5)

        btn_agregar = tk.Button(frame_entrada, text="Agregar", command=self.agregar_item)
        btn_agregar.pack(side=tk.LEFT)

        # Listbox: Lista visual de elementos
        self.lista = tk.Listbox(self, width=40, height=15)
        self.lista.pack(padx=10, pady=10)

        # Agregar algunos datos iniciales
        self.lista.insert(tk.END, "Elemento 1")
        self.lista.insert(tk.END, "Elemento 2")

    def agregar_item(self):
        nuevo = self.entrada_item.get()
        if nuevo:
            self.lista.insert(tk.END, nuevo) # Insertar al final
            self.entrada_item.delete(0, tk.END) # Limpiar entrada


class Ejercicio5(tk.Toplevel):
    """
    5. Canvas para dibujar líneas con el mouse.
    """
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Ejercicio 5: Pizarra de Dibujo")
        self.geometry("500x400")

        tk.Label(self, text="Mantén presionado el clic izquierdo para dibujar").pack()
        
        # Canvas: Área de dibujo
        self.canvas = tk.Canvas(self, bg="white", width=480, height=350, cursor="pencil")
        self.canvas.pack(pady=10)

        # Variables para guardar la posición anterior del mouse
        self.last_x, self.last_y = None, None

        # Vincular eventos del mouse
        self.canvas.bind('<Button-1>', self.guardar_inicio) # Clic presionado
        self.canvas.bind('<B1-Motion>', self.dibujar)       # Mover mouse con clic

    def guardar_inicio(self, event):
        # Guardar coordenadas donde se hizo clic
        self.last_x, self.last_y = event.x, event.y

    def dibujar(self, event):
        if self.last_x and self.last_y:
            # Dibujar línea desde la posición anterior a la actual
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y, 
                                  width=2, fill="black", capstyle=tk.ROUND, smooth=True)
            # Actualizar posición anterior
            self.last_x, self.last_y = event.x, event.y


class AppPrincipal(tk.Tk):
    """
    Ventana Principal (Menú) para lanzar los ejercicios.
    """
    def __init__(self):
        super().__init__()
        self.title("Menú de Ejercicios Tkinter")
        self.geometry("300x400")

        tk.Label(self, text="Selecciona un ejercicio", font=("Arial", 14)).pack(pady=20)

        # Botones para abrir cada ejercicio
        tk.Button(self, text="1. Mensaje Bienvenida", command=lambda: Ejercicio1(self), width=25).pack(pady=5)
        tk.Button(self, text="2. Entry y Botón", command=lambda: Ejercicio2(self), width=25).pack(pady=5)
        tk.Button(self, text="3. Calculadora Suma", command=lambda: Ejercicio3(self), width=25).pack(pady=5)
        tk.Button(self, text="4. Listbox Dinámico", command=lambda: Ejercicio4(self), width=25).pack(pady=5)
        tk.Button(self, text="5. Canvas (Dibujo)", command=lambda: Ejercicio5(self), width=25).pack(pady=5)
        
        tk.Button(self, text="Salir", command=self.quit, bg="red", fg="white").pack(pady=30)

if __name__ == "__main__":
    app = AppPrincipal()
    app.mainloop()