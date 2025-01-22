#sintaxis tradicional
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
impares = []
for num in numeros:
    if num % 2 != 0:
        impares.append(num)
print(impares)

#usando comprension
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
impares = [num for num in numeros if num % 2 != 0]
print(impares)
