class Curso:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor
        self.estudiantes = []

    def inscribir_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        print(f"{estudiante} ha sido inscrito en el curso {self.nombre}.")

    def mostrar_estudiantes(self):
        print(f"Estudiantes en el curso {self.nombre}:")
        for estudiante in self.estudiantes:
            print(f"- {estudiante}")

curso = Curso("Introducción a la Programación", "Profesor Pérez")
curso.inscribir_estudiante("Juan")
curso.inscribir_estudiante("Ana")
curso.mostrar_estudiantes()
