#Carrito de compras:
carrito = {}
while True:
    producto = input("Ingresa un producto (o 'salir' para terminar): ")
    if producto == "salir":
        break
    precio = float(input(f"Precio de {producto}: "))
    carrito[producto] = precio

total = sum(carrito.values())
print("Productos en el carrito:", carrito)
print("Total a pagar:", total)