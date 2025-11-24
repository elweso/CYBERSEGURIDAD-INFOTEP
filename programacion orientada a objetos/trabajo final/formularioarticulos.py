import tkinter as tk
from tkinter import messagebox as mb
import articulos


class App:
    def __init__(self):
        self.art = articulos.Articulos()
        
        self.ventana = tk.Tk()
        self.ventana.title("Gestión Artículos")
        self.ventana.geometry("400x300")
        
        # Botón para ver códigos
        tk.Button(self.ventana, text="Ver todos los artículos",
                  command=self.ver_todo, width=30, height=2).pack(pady=10)
        
        # Búsqueda por código
        tk.Label(self.ventana, text="Buscar por código:").pack()
        self.entrada_cod = tk.Entry(self.ventana, width=20)
        self.entrada_cod.pack(pady=5)
        
        tk.Button(self.ventana, text="Buscar",
                  command=self.buscar, width=30).pack(pady=5)
        
        # Agregar artículo
        tk.Label(self.ventana, text="Descripción:").pack(pady=(10, 0))
        self.entrada_desc = tk.Entry(self.ventana, width=30)
        self.entrada_desc.pack(pady=5)
        
        tk.Label(self.ventana, text="Precio:").pack()
        self.entrada_prec = tk.Entry(self.ventana, width=30)
        self.entrada_prec.pack(pady=5)
        
        tk.Button(self.ventana, text="Agregar Artículo",
                  command=self.agregar, width=30).pack(pady=10)
        
        self.ventana.mainloop()
    
    def ver_todo(self):
        try:
            datos = self.art.recuperar_todos()
            if not datos:
                mb.showinfo("Info", "No hay artículos")
                return
            
            msg = "ARTÍCULOS:\n\n"
            for cod, desc, prec in datos:
                msg += f"Código {cod}: {desc} - ${prec}\n"
            
            mb.showinfo("Artículos", msg)
        except Exception as e:
            mb.showerror("Error", str(e))
    
    def buscar(self):
        try:
            cod = int(self.entrada_cod.get())
            resultado = self.art.consulta((cod,))
            
            if resultado:
                desc, prec = resultado[0]
                msg = f"Código: {cod}\nDescripción: {desc}\nPrecio: ${prec}"
                mb.showinfo("Encontrado", msg)
            else:
                mb.showinfo("No encontrado", f"No existe código {cod}")
        except ValueError:
            mb.showerror("Error", "Ingrese un código numérico")
        except Exception as e:
            mb.showerror("Error", str(e))
    
    def agregar(self):
        try:
            desc = self.entrada_desc.get().strip()
            prec = float(self.entrada_prec.get())
            
            if not desc:
                mb.showerror("Error", "Ingrese descripción")
                return
            if prec <= 0:
                mb.showerror("Error", "Precio debe ser > 0")
                return
            
            self.art.alta((desc, prec))
            msg = f"Artículo '{desc}' agregado"
            mb.showinfo("Éxito", msg)
            self.entrada_desc.delete(0, tk.END)
            self.entrada_prec.delete(0, tk.END)
        except ValueError:
            mb.showerror("Error", "Precio debe ser un número")
        except Exception as e:
            mb.showerror("Error", str(e))


if __name__ == "__main__":
    app = App()
