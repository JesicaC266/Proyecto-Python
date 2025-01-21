texto = "Hola, ¿cómo estás?"

vocales = "aeiouAEIOU"
contador_vocales = 0

for caracter in texto:
    if caracter in vocales:
        contador_vocales += 1

print(f"El número de vocales en el texto es: {contador_vocales}")
