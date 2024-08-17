# Gestor de Tareas

# Función para mostrar el menú
def mostrar_menu():
    print("\nGestor de Tareas")
    print("1. Agregar una tarea")
    print("2. Ver todas las tareas")
    print("3. Marcar una tarea como completada")
    print("4. Guardar tareas en archivo")
    print("5. Cargar tareas desde archivo")
    print("6. Salir")

# Función para agregar una tarea
def agregar_tarea(tareas):
    descripcion = input("Descripción de la tarea: ")
    fecha_limite = input("Fecha límite (dd/mm/yyyy): ")
    tarea = {
        "descripcion": descripcion,
        "fecha_limite": fecha_limite,
        "completada": False
    }
    tareas.append(tarea)
    print("Tarea agregada exitosamente.")

# Función para ver todas las tareas
def ver_tareas(tareas):
    if not tareas:
        print("No hay tareas.")
        return

    for i, tarea in enumerate(tareas, start=1):
        estado = "Completada" if tarea["completada"] else "Pendiente"
        print(f"{i}. {tarea['descripcion']} (Fecha límite: {tarea['fecha_limite']}) - {estado}")

# Función para marcar una tarea como completada
def completar_tarea(tareas):
    ver_tareas(tareas)
    numero_tarea = int(input("Número de la tarea a marcar como completada: ")) - 1

    if 0 <= numero_tarea < len(tareas):
        tareas[numero_tarea]["completada"] = True
        print("Tarea marcada como completada.")
    else:
        print("Número de tarea inválido.")

# Función para guardar las tareas en un archivo
def guardar_tareas(tareas):
    with open("tareas.txt", "w") as archivo:
        for tarea in tareas:
            archivo.write(f"{tarea['descripcion']}|{tarea['fecha_limite']}|{tarea['completada']}\n")
    print("Tareas guardadas en archivo.")

# Función para cargar las tareas desde un archivo
def cargar_tareas():
    tareas = []
    try:
        with open("tareas.txt", "r") as archivo:
            for linea in archivo:
                descripcion, fecha_limite, completada = linea.strip().split("|")
                tarea = {
                    "descripcion": descripcion,
                    "fecha_limite": fecha_limite,
                    "completada": completada == "True"
                }
                tareas.append(tarea)
    except FileNotFoundError:
        print("Archivo no encontrado. Comenzando con lista de tareas vacía.")
    return tareas

# Programa principal
def main():
    tareas = cargar_tareas()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregar_tarea(tareas)
        elif opcion == "2":
            ver_tareas(tareas)
        elif opcion == "3":
            completar_tarea(tareas)
        elif opcion == "4":
            guardar_tareas(tareas)
        elif opcion == "5":
            tareas = cargar_tareas()
        elif opcion == "6":
            print("Saliendo del gestor de tareas.")
            break
        else:
            print("Opción inválida. Por favor, intenta nuevamente.")

if __name__ == "__main__":
    main()

    


    