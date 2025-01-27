class Pelota:
    def __init__(self, color, tamaño):
        self.color = color
        self.tamaño = tamaño
        self.rebota = False

    def rebotar(self):
        self.rebota = True
        print(f"La pelota de color {self.color} está rebotando.")

    def detener(self):
        self.rebota = False
        print(f"La pelota de color {self.color} ha dejado de rebotar.")

    def cambiar_color(self, nuevo_color):
        self.color = nuevo_color
        print(f"La pelota ahora es de color {self.color}.")


mi_pelota = Pelota("roja", "mediana")
mi_pelota.rebotar()
mi_pelota.cambiar_color("azul")
mi_pelota.detener()
