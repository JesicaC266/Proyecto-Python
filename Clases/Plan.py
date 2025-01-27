class Plan:
    def __init__(self, nombre, fecha):
        self.nombre = nombre
        self.fecha = fecha
        self.actividades = []

    def agregar_actividad(self, actividad):
        self.actividades.append(actividad)
        print(f"Actividad '{actividad}' agregada al plan {self.nombre}.")

    def mostrar_plan(self):
        print(f"Plan: {self.nombre} (Fecha: {self.fecha})")
        for actividad in self.actividades:
            print(f"- {actividad}")

plan = Plan("Vacaciones de verano", "2025-06-01")
plan.agregar_actividad("Ir a la playa")
plan.agregar_actividad("Visitar museos")
plan.mostrar_plan()
