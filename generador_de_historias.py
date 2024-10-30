import random

# Listas iniciales de personajes, lugares y acciones
personajes = ["un mago", "una princesa", "un dragón"]
lugares = ["en el castillo", "en el bosque encantado", "en la cueva oscura"]
acciones = ["luchó valientemente", "exploró con curiosidad", "se escondió rápidamente"]

def agregar_nuevo_elemento(lista, tipo):
    nuevo_elemento = input(f"Ingrese un nuevo {tipo}: ")
    lista.append(nuevo_elemento)
    print(f"Se ha agregado {nuevo_elemento} a la lista de {tipo}s.\n")

def generar_historia():
    personaje = random.choice(personajes)
    lugar = random.choice(lugares)
    accion = random.choice(acciones)
    historia = f"Había una vez {personaje} que {accion} {lugar}."
    return historia

# Bucle principal para interactuar con el usuario
while True:
    print("\nMenú:")
    print("1. Agregar un nuevo personaje")
    print("2. Agregar un nuevo lugar")
    print("3. Agregar una nueva acción")
    print("4. Generar una historia aleatoria")
    print("5. Salir")

    opcion = input("Seleccione una opción (1-5): ")

    if opcion == "1":
        agregar_nuevo_elemento(personajes, "personaje")
    elif opcion == "2":
        agregar_nuevo_elemento(lugares, "lugar")
    elif opcion == "3":
        agregar_nuevo_elemento(acciones, "acción")
    elif opcion == "4":
        print("\n" + generar_historia())
    elif opcion == "5":
        print("¡Gracias por jugar! Hasta la próxima.")
        break
    else:
        print("Opción no válida. Por favor, seleccione nuevamente.")
