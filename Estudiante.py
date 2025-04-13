from Lista import Lista

class Estudiante:
    def __init__(self,identificacion, nombre, edad):
        self.identificacion = identificacion
        self.nombre = nombre
        self.edad = edad
        self.materias = []
        
    def agregar_materia(self, materia):
        self.materias.append(materia)
        
    def eliminar_materia(self, materia):
        if materia in self.materias:
            self.materias.remove(materia)