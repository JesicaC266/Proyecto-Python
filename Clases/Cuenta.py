class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Se han depositado {cantidad} euros en la cuenta de {self.titular}.")
        else:
            print("La cantidad a depositar debe ser mayor a 0.")

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Se han retirado {cantidad} euros de la cuenta de {self.titular}.")
        else:
            print("Saldo insuficiente o cantidad no válida.")

    def mostrar_saldo(self):
        print(f"El saldo actual de la cuenta de {self.titular} es {self.saldo} euros.")

mi_cuenta = CuentaBancaria("Juan", 500)
mi_cuenta.mostrar_saldo()
mi_cuenta.depositar(200)
mi_cuenta.retirar(100)
mi_cuenta.mostrar_saldo()
