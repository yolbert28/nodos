import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class GraphEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor de Grafos Dinámico")
        
        # Crear el grafo
        self.G = nx.Graph()
        self.G.add_nodes_from([1, 2, 3])  # Nodos iniciales
        self.G.add_edges_from([(1, 2), (2, 3)])  # Conexiones iniciales
        
        # Configurar la figura de Matplotlib
        self.fig, self.ax = plt.subplots(figsize=(6, 4))
        self.pos = nx.spring_layout(self.G)  # Diseño inicial
        
        # Canvas para el gráfico
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        # Frame para controles
        self.control_frame = ttk.Frame(root)
        self.control_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=5)
        
        # Entradas para nodos y conexiones
        ttk.Label(self.control_frame, text="Nodo:").grid(row=0, column=0)
        self.nodo_entry = ttk.Entry(self.control_frame, width=5)
        self.nodo_entry.grid(row=0, column=1)
        
        ttk.Label(self.control_frame, text="Conexión (n1,n2):").grid(row=0, column=2)
        self.conexion_entry = ttk.Entry(self.control_frame, width=10)
        self.conexion_entry.grid(row=0, column=3)
        
        # Botones
        ttk.Button(self.control_frame, text="Agregar Nodo", 
                  command=self.agregar_nodo).grid(row=1, column=0, columnspan=2, pady=5)
        ttk.Button(self.control_frame, text="Agregar Conexión", 
                  command=self.agregar_conexion).grid(row=1, column=2, columnspan=2, pady=5)
        
        # Dibujar el grafo inicial
        self.dibujar_grafo()
    
    def dibujar_grafo(self):
        self.ax.clear()  # Limpiar el eje anterior
        nx.draw(self.G, self.pos, ax=self.ax, with_labels=True, 
                node_color='skyblue', node_size=800, font_weight='bold')
        self.canvas.draw()
    
    def agregar_nodo(self):
        try:
            nuevo_nodo = int(self.nodo_entry.get())
            if nuevo_nodo not in self.G.nodes():
                self.G.add_node(nuevo_nodo)
                self.pos = nx.spring_layout(self.G)  # Recalcular posiciones
                self.dibujar_grafo()
        except ValueError:
            print("Ingresa un número válido para el nodo")
    
    def agregar_conexion(self):
        try:
            n1, n2 = map(int, self.conexion_entry.get().split(','))
            if n1 in self.G.nodes() and n2 in self.G.nodes():
                self.G.add_edge(n1, n2)
                self.pos = nx.spring_layout(self.G)  # Recalcular posiciones
                self.dibujar_grafo()
        except ValueError:
            print("Formato incorrecto. Usa: numero,numero")

# Iniciar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = GraphEditor(root)
    root.mainloop()