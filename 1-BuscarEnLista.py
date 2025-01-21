#Buscar un elemento en una lista:
numeros = [3, 7, 12, 18, 25]
buscar = int(input("Ingresa el número a buscar: "))

encontrado = False
for num in numeros:
    if num == buscar:
        encontrado = True
        break

if encontrado:
    print(f"El numerito {buscar} está en la lista.")
else:
    print(f"El numerito {buscar} no está en la lista.")
    #esta es una prueba