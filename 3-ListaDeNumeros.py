#Promedio de una lista de números
def calcular_promedio(lista):
    return sum(lista) / len(lista)

numeros = [10, 20, 30, 40]
print("El promedio es:", calcular_promedio(numeros))
