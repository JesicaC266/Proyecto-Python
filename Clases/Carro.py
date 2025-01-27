class Coche:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0

    def arrancar(self):
        print(f"El {self.marca} {self.modelo} ha arrancado.")

    def frenar(self):
        print(f"El {self.marca} {self.modelo} ha frenado.")
        self.velocidad = 0

    def acelerar(self, incremento):
        self.velocidad += incremento
        print(f"El {self.marca} {self.modelo} está a {self.velocidad} km/h.")

# Crear una instancia de la clase Coche
mi_coche = Coche("Toyota", "Corolla")
mi_coche.arrancar()
mi_coche.acelerar(50)
mi_coche.frenar()
