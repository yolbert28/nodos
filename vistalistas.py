import tkinter as tk
from tkinter import messagebox
from Lista import Lista  # Asegúrate de importar correctamente
from Estudiante import Estudiante  # Asegúrate de importar correctamente

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Lista Enlazada Visual")
ventana.minsize(1300,800)
ventana.grid_rowconfigure(0, weight=1)

# Crear lista
lista = Lista()

# Crear frames para cada columna
columna1 = tk.Frame(ventana)
columna2 = tk.Frame(ventana,)

# Empacar los frames lado a lado
columna1.pack(side="left", fill="both", expand=True)
columna2.pack(side="left", fill="y", expand=True)

# Canvas para dibujar
canvas = tk.Canvas(columna1, bg="white")
canvas.pack(fill=tk.BOTH, padx=20, pady=20, expand=True)

# Variables para selección
nodo_seleccionado = None
        
def dibujar_lista_estudiante():
    global nodo_seleccionado
    canvas.delete("all")
    print("dibujar lista estudiante")
    if lista.Vacia():
        canvas.create_text((canvas.winfo_reqwidth() / 2), (canvas.winfo_reqheight() / 2), text="[Lista vacía]", font=("Arial", 14))
        return
    
    x = 100  # Posición inicial X
    y = 150  # Posición fija Y
    separacion = 100  # Espacio entre nodos
    
    p = lista.Primero
    while p is not None:
        # Dibujar nodo (círculo + texto)
        color = "red" if p == lista.Primero else ("lightgreen" if p == nodo_seleccionado else "lightblue")
        canvas.create_oval(x-30, y-30, x+30, y+30, fill=color, tags=f"nodo_{p.info.identificacion}")
        canvas.create_text(x, y, text=str(p.info.identificacion), font=("Arial", 12))
        
        # Dibujar flecha si hay próximo nodo
        if p.prox is not None:
            canvas.create_line(x+30, y, x+separacion-30, y, arrow=tk.LAST)
        
        # Etiquetar cabeza
        if p == lista.Primero:
            canvas.create_text(x, y-50, text="Primero", fill="red", font=("Arial", 10, "bold"))
        
        # Asignar evento de clic para selección
        canvas.tag_bind(f"nodo_{p.info.identificacion}", "<Button-1>", lambda e, nodo=p: seleccionar_nodo(nodo))
        
        x += separacion
        p = p.prox

# Selección de nodo
def seleccionar_nodo(nodo):
    global nodo_seleccionado
    nodo_seleccionado = nodo
    dibujar_lista_estudiante()
    
def fill_fields():
    if nodo_seleccionado is not None:
        identificacion_entry.config(state='normal')
        nombre_entry.config(state='normal')
        edad_entry.config(state='normal')
        materias_entry.config(state='normal')
        
        identificacion_entry.delete(0, tk.END)
        nombre_entry.delete(0, tk.END)
        edad_entry.delete(0, tk.END)
        materias_entry.delete(0, tk.END)
        
        identificacion_entry.insert(0, nodo_seleccionado.info.identificacion)
        nombre_entry.insert(0, nodo_seleccionado.info.nombre)
        edad_entry.insert(0, nodo_seleccionado.info.edad)
        materias_entry.insert(0, ", ".join(nodo_seleccionado.info.materias))
    
    identificacion_entry.config(state='readonly')
    nombre_entry.config(state='readonly')
    edad_entry.config(state='readonly')
    materias_entry.config(state='readonly')
    
def limpiar():
    seleccionar_nodo(None)
    identificacion_entry.config(state='normal')
    nombre_entry.config(state='normal')
    edad_entry.config(state='normal')
    materias_entry.config(state='normal')
        
    identificacion_entry.delete(0, tk.END)
    nombre_entry.delete(0, tk.END)
    edad_entry.delete(0, tk.END)
    materias_entry.delete(0, tk.END)
    
# Insertar al inicio
def insertar_inicio_estudiante():
    identificacion = identificacion_entry.get()
    nombre = nombre_entry.get()
    edad = edad_entry.get()
    
    estudiante = None
    
    if identificacion and nombre and edad:
        estudiante = Estudiante(identificacion, nombre, edad)
    
    if estudiante is not None:
        if lista.InsComienzo(estudiante):
            dibujar_lista_estudiante()
        else:
            messagebox.showerror("Error", "¡Memoria llena!")
    else:
        messagebox.showwarning("Advertencia", "Ingresa un valor.")
    limpiar()

# Eliminar al inicio
def eliminar_inicio_estudiante():
    if lista.Vacia():
        messagebox.showinfo("Info", "Lista vacía")
    else:
        lista.EliComienzo()
        dibujar_lista_estudiante()

# Insertar después del seleccionado
def insertar_despues_estudiante():
    if nodo_seleccionado is None:
        messagebox.showwarning("Advertencia", "Selecciona un nodo primero")
        return
    
    identificacion = identificacion_entry.get()
    nombre = nombre_entry.get()
    edad = edad_entry.get()
    
    estudiante = None
    
    if identificacion and nombre and edad:
        estudiante = Estudiante(identificacion, nombre, edad)
    
    if identificacion:
        if lista.InsDespues(nodo_seleccionado, estudiante):
            dibujar_lista_estudiante()
        else:
            messagebox.showerror("Error", "¡Memoria llena!")
    else:
        messagebox.showwarning("Advertencia", "Ingresa un valor.")
    limpiar()

# Eliminar después del seleccionado
def eliminar_despues_estudiante():
    if nodo_seleccionado is None:
        messagebox.showwarning("Advertencia", "Selecciona un nodo primero")
    else:
        valor = lista.EliDespues(nodo_seleccionado)
        if valor is None:
            messagebox.showinfo("Info", "No hay nodo siguiente")
        dibujar_lista_estudiante()
        
def agregar_materia():
    if nodo_seleccionado is None:
        messagebox.showwarning("Advertencia", "Selecciona un nodo primero")
        return
    
    materia = materias_entry.get()
    
    if materia:
        nodo_seleccionado.info.agregar_materia(materia)
    else:
        messagebox.showwarning("Advertencia", "Ingresa una materia.")
    
    materias_entry.delete(0, tk.END)
    
def eliminar_materia():
    if nodo_seleccionado is None:
        messagebox.showwarning("Advertencia", "Selecciona un nodo primero")
        return
    
    materia = materias_entry.get()
    
    if materia:
        nodo_seleccionado.info.eliminar_materia(materia)
    else:
        messagebox.showwarning("Advertencia", "Ingresa una materia.")
    
    materias_entry.delete(0, tk.END)

frame_normal = tk.Frame(columna2)
frame_normal.pack(padx=20, pady=20)

# Interfaz
frame_botones_estudiante = tk.Frame(frame_normal)
frame_botones_estudiante.pack()

frame_botones_estudiante1 = tk.Frame(frame_normal)
frame_botones_estudiante1.pack()

frame_botones_estudiante2 = tk.Frame(frame_normal)
frame_botones_estudiante2.pack()

frame_entry_estudiante = tk.Frame(frame_normal)
frame_entry_estudiante.pack(side=tk.BOTTOM)

tk.Button(frame_botones_estudiante, text="Insertar Inicio", command=insertar_inicio_estudiante, width= 15).pack(side=tk.LEFT, pady=5, padx=10)
tk.Button(frame_botones_estudiante, text="Eliminar Inicio", command=eliminar_inicio_estudiante, width= 15).pack(side=tk.LEFT, pady=5, padx=10)
tk.Button(frame_botones_estudiante1, text="Insertar Después", command=insertar_despues_estudiante, width= 15).pack(side=tk.LEFT, pady=5, padx=10)
tk.Button(frame_botones_estudiante1, text="Eliminar Después", command=eliminar_despues_estudiante, width= 15).pack(side=tk.LEFT, pady=5, padx=10)
tk.Button(frame_botones_estudiante2, text="Limpiar", command=limpiar, width= 15).pack(side=tk.LEFT,pady=5, padx=10)
tk.Button(frame_botones_estudiante2, text="Ver info", command=fill_fields, width= 15).pack(side=tk.LEFT,pady=5, padx=10)

frame_entry_estudiante_1 = tk.Frame(frame_entry_estudiante)
frame_entry_estudiante_1.pack()

frame_entry_estudiante_2 = tk.Frame(frame_entry_estudiante)
frame_entry_estudiante_2.pack()

frame_entry_estudiante_3 = tk.Frame(frame_entry_estudiante)
frame_entry_estudiante_3.pack()

frame_botones_estudiante3 = tk.Frame(frame_entry_estudiante)
frame_botones_estudiante3.pack()

frame_entry_estudiante_4 = tk.Frame(frame_entry_estudiante)
frame_entry_estudiante_4.pack()

text_valor = tk.Label(frame_entry_estudiante_1, text="Identificacion: ")
text_valor.pack(side=tk.LEFT, pady=5)

identificacion_entry = tk.Entry(frame_entry_estudiante_1, width=30)
identificacion_entry.pack(side=tk.LEFT, pady=5)

text_valor = tk.Label(frame_entry_estudiante_2, text="Nombre: ")
text_valor.pack(side=tk.LEFT, pady=5)

nombre_entry = tk.Entry(frame_entry_estudiante_2, width=30)
nombre_entry.pack(side=tk.LEFT, pady=5)

text_valor = tk.Label(frame_entry_estudiante_3, text="Edad: ")
text_valor.pack(side=tk.LEFT, pady=5)

edad_entry = tk.Entry(frame_entry_estudiante_3, width=30)
edad_entry.pack(side=tk.LEFT, pady=5)

tk.Button(frame_botones_estudiante3, text="Agregar materia", command=agregar_materia, width= 15).pack(side=tk.LEFT,pady=5, padx=10)
tk.Button(frame_botones_estudiante3, text="Eliminar materia", command=eliminar_materia, width= 15).pack(side=tk.LEFT,pady=5, padx=10)

text_valor = tk.Label(frame_entry_estudiante_4, text="Materias: ")
text_valor.pack(side=tk.LEFT, pady=5)

materias_entry = tk.Entry(frame_entry_estudiante_4, width=30)
materias_entry.pack(side=tk.LEFT, pady=5)

# Mostrar lista inicial
dibujar_lista_estudiante()
ventana.mainloop()