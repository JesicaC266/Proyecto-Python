numeros = [3,7,2,9,5]
buscar=7
encontrado= False

for numero in numeros:
    if numero == buscar:
        encontrado = True
        break
    
if encontrado:
    print (f"El número {buscar} está en la lista.")
else:
    print(f"El número {buscar} no está en la lista.")


