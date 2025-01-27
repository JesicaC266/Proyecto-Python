class Carro:
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
        self.frenar = True

    def movimiento(self):
        self.frenar = False
        print(f"el carro color {self.color} está en movimiento")

    def freno(self):
        self.frenar = True
        print(f"el carro color {self.color} está quieto")

    def cambio_color(self,nuevo_color):
        self.color = nuevo_color
        print(f"el carro ahora es de color {self.color}.")
        
el_carro = Carro("suzuki", "rojo")
el_carro.movimiento()
el_carro.cambio_color("gris")
el_carro.freno()
