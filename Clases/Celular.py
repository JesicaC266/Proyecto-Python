class Telefono:
    def __init__(self, marca, modelo, numero_telefono):
        self.marca = marca
        self.modelo = modelo
        self.numero_telefono = numero_telefono

    def hacer_llamada(self, numero_destino):
        print(f"Marcando al número {numero_destino} desde el teléfono {self.numero_telefono}... Llamada en curso.")

    def enviar_mensaje(self, numero_destino, mensaje):
        print(f"Enviando mensaje a {numero_destino}: {mensaje}")


mi_telefono = Telefono("Samsung", "Galaxy S22", "123-456-7890")
mi_telefono.hacer_llamada("987-654-3210")
mi_telefono.enviar_mensaje("987-654-3210", "Hola, ¿cómo estás?")
