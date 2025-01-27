class Emocion:
    def __init__(self, nombre, intensidad):
        self.nombre = nombre
        self.intensidad = intensidad

    def cambiar_emocion(self, nueva_emocion, nueva_intensidad):
        self.nombre = nueva_emocion
        self.intensidad = nueva_intensidad
        print(f"Ahora estoy sintiendo {self.nombre} con una intensidad de {self.intensidad}.")

    def mostrar_emocion(self):
        print(f"Mi emoción actual es {self.nombre} con una intensidad de {self.intensidad}.")

emocion = Emocion("felicidad", 8)
emocion.mostrar_emocion()
emocion.cambiar_emocion("tristeza", 5)
emocion.mostrar_emocion()
