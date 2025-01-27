class Vaso:
    def __init__(self, material, capacidad):
        self.material = material
        self.capacidad = capacidad
        self.contenido = 0

    def llenar(self, cantidad):
        if cantidad <= self.capacidad - self.contenido:
            self.contenido += cantidad
            print(f"El vaso ahora tiene {self.contenido} litros.")
        else:
            print("No hay suficiente espacio en el vaso.")

    def vaciar(self):
        self.contenido = 0
        print("El vaso está vacío.")

mi_vaso = Vaso("vidrio", 1)
mi_vaso.llenar(0.5)
mi_vaso.vaciar()
