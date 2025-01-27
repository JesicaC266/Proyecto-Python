class Concierto:
    def __init__(self, artista, lugar, fecha, entradas_totales):
        self.artista = artista
        self.lugar = lugar
        self.fecha = fecha
        self.entradas_totales = entradas_totales
        self.entradas_vendidas = 0

    def vender_entradas(self, cantidad):
        if cantidad <= (self.entradas_totales - self.entradas_vendidas):
            self.entradas_vendidas += cantidad
            print(f"Se han vendido {cantidad} entradas. Total de entradas vendidas: {self.entradas_vendidas}.")
        else:
            print("No hay suficientes entradas disponibles.")

    def mostrar_evento(self):
        print(f"Concierto de {self.artista} en {self.lugar} el {self.fecha}. Entradas disponibles: {self.entradas_totales - self.entradas_vendidas}.")

concierto = Concierto("Shakira", "Estadio Nacional", "2025-03-15", 5000)
concierto.mostrar_evento()
concierto.vender_entradas(1000)
concierto.mostrar_evento()
