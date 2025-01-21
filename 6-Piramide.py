filas = 5

for i in range(1, filas + 1):
    # Imprimir espacios antes de los asteriscos
    espacios = " " * (filas - i)
    # Imprimir asteriscos
    asteriscos = "*" * (2 * i - 1)
    print(espacios + asteriscos)
