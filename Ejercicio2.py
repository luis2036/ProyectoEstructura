import tkinter as tk
from tkinter import simpledialog, messagebox
from TDAs import Grafo

class AppMapa:
    def __init__(self, master):
        self.master = master
        self.master.title("Mapa Interactivo")

        self.grafo = Grafo()

        self.crear_menu()

        self.canvas = tk.Canvas(master, width=800, height=600)
        self.canvas.pack()

    def crear_menu(self):
        self.menu_bar = tk.Menu(self.master)

        # Menú Archivo
        self.archivo_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.archivo_menu.add_command(label="Agregar Ubicación", command=self.agregar_ubicacion)
        self.archivo_menu.add_command(label="Agregar Conexión", command=self.agregar_conexion)
        self.archivo_menu.add_separator()
        self.archivo_menu.add_command(label="Encontrar Camino Más Corto", command=self.encontrar_camino_mas_corto)
        self.archivo_menu.add_separator()
        self.archivo_menu.add_command(label="Salir", command=self.master.quit)
        self.menu_bar.add_cascade(label="Archivo", menu=self.archivo_menu)

        # Menú Ayuda
        self.ayuda_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.ayuda_menu.add_command(label="Acerca de", command=self.acerca_de)
        self.menu_bar.add_cascade(label="Ayuda", menu=self.ayuda_menu)

        self.master.config(menu=self.menu_bar)

    def acerca_de(self):
        messagebox.showinfo("Acerca de", "Mapa Interactivo - Versión 1.0")

    def dibujar_mapa(self):
        self.canvas.delete("all")
        for nodo in self.grafo.nodos.values():
            x, y = nodo.x, nodo.y
            self.canvas.create_oval(x-10, y-10, x+10, y+10, fill="blue")
            self.canvas.create_text(x, y, text=nodo.nombre, fill="white")

        for nodo in self.grafo.nodos:
            for vecino, peso in self.grafo.aristas[nodo]:
                x1, y1 = self.grafo.obtener_coordenadas_nodo(nodo)
                x2, y2 = self.grafo.obtener_coordenadas_nodo(vecino)
                self.canvas.create_line(x1, y1, x2, y2)

    def agregar_ubicacion(self):
        nombre = simpledialog.askstring("Nombre de la Ubicación", "Ingrese el nombre de la ubicación:")
        x = simpledialog.askinteger("Coordenada X", "Ingrese la coordenada X:")
        y = simpledialog.askinteger("Coordenada Y", "Ingrese la coordenada Y:")
        if nombre and x is not None and y is not None:
            self.grafo.agregar_nodo(nombre, x, y)
            self.dibujar_mapa()

    def agregar_conexion(self):
        nodo1 = simpledialog.askstring("Ubicación 1", "Ingrese el nombre de la primera ubicación:")
        nodo2 = simpledialog.askstring("Ubicación 2", "Ingrese el nombre de la segunda ubicación:")
        peso = simpledialog.askinteger("Peso de la Conexión", "Ingrese el peso de la conexión:")
        if nodo1 and nodo2 and peso is not None:
            self.grafo.agregar_arista(nodo1, nodo2, peso)
            self.dibujar_mapa()

    def encontrar_camino_mas_corto(self):
        inicio = simpledialog.askstring("Inicio", "Ingrese el nombre de la ubicación de inicio:")
        fin = simpledialog.askstring("Fin", "Ingrese el nombre de la ubicación de fin:")
        if inicio and fin:
            resultado = self.grafo.obtener_camino_mas_corto(inicio, fin)
            if resultado:
                camino, distancia = resultado
                messagebox.showinfo("Camino Más Corto", f"El camino más corto es: {' -> '.join(camino)} con una distancia de {distancia}")
            else:
                messagebox.showinfo("Camino Más Corto", "No se encontró un camino entre las ubicaciones especificadas.")

def main():
    root = tk.Tk()
    app = AppMapa(root)
    root.mainloop()

if __name__ == "__main__":
    main()
