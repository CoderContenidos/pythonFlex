'''
### Gestión de Tareas Pendientes (Con persistencia de datos)

Basandonos en el ejercicio 1 de la semana 5 (funciones), editar el codigo para que 
el programa guarde el listado de tareas en un json al terminar la ejecucion del programa y 
lo recupere al iniciarse el mismo.


nota
->  Tener en cuenta que el modo read del open genera un error al querer abrir un arhcivo que no existe.
    Y, a diferencia del read en los txt, el json.load tambien genera un erorr si el archivo no tiene nada.

'''

import json

def agregar_tarea(tareas, tarea):
    # Agrega una nueva tarea a la lista "tareas".
    tareas.append(tarea)

def marcar_completada(tareas, indice):
    # Marca una tarea como completada agregando "✔" al principio.
    if 0 <= indice < len(tareas):
        tareas[indice] = "✔ " + tareas[indice]

def listar_tareas(tareas):
    # Muestra las tareas pendientes numeradas.
    for i, tarea in enumerate(tareas):
        print(f"{i + 1}. {tarea}")

try:
    with open('tareas_pendientes.json', 'r') as archivo:
        tareas_pendientes = json.load(archivo)
except Exception as err:
    tareas_pendientes = []  # Lista para almacenar tareas pendientes.
        

while True:
    print("\n1. Agregar tarea")
    print("2. Marcar tarea como completada")
    print("3. Listar tareas pendientes")
    print("4. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == '1':
        tarea = input("Ingresa la tarea pendiente: ")
        agregar_tarea(tareas_pendientes, tarea)
        print("Tarea agregada.")
    elif opcion == '2':
        listar_tareas(tareas_pendientes)
        indice = int(input("Ingresa el número de la tarea completada: ")) - 1
        marcar_completada(tareas_pendientes, indice)
        print("Tarea marcada como completada.")
    elif opcion == '3':
        listar_tareas(tareas_pendientes)
    elif opcion == '4':
        break

with open('tareas_pendientes.json', 'w') as archivo:
    json.dump(tareas_pendientes, archivo, indent=4)