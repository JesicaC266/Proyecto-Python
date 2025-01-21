def calcular_promedio(*args):
    if len(args) == 0:
        return "No se proporcionaron números"
    suma = sum(args)
    promedio = suma / len(args)
    return promedio

print(calcular_promedio(1, 2, 3, 4, 5))  
print(calcular_promedio(10, 20, 30))     
print(calcular_promedio())
