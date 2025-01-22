#Simular una fila de personas:
 fila= []
while True:
    accion = input("¿Agregar o eliminar persona? (agregar/eliminar/salir): ").lower()
    if accion == "agregar":
        persona = input("Nombre de la persona: ")
        fila.append(persona)
    elif accion == "eliminar":
        if fila:
            print("Persona eliminada:", fila.pop(0))
        else:
            print("La fila está vacía.")
    elif accion == "salir":
        break
    else:
        print("Acción no válida.")
    
    print("Fila actual:", fila)
