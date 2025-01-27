class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"¡Hola! Soy {self.nombre} y tengo {self.edad} años.")

persona1 = Persona("Carlos", 30)
persona1.saludar()

