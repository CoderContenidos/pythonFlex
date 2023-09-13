'''
### Registro de calificaciones
Escribe un programa que permita a un profesor registrar las calificaciones de sus estudiantes en un archivo json llamado "calificaciones.json".
El programa debe permitir al profesor ingresar nombres de estudiantes y sus calificaciones. Luego, debe guardar estos datos en el archivo cuando termine el programa para 
persistir estos datos para futuras ejecuciones del programa. Utilizar los nombres de los alumnos como claves y las notas como valores.

nota
->  Tener en cuenta que el modo read del open genera un error al querer abrir un arhcivo que no existe.
    Y, a diferencia del read en los txt, el json.load tambien genera un erorr si el archivo no tiene nada.

'''
import json

# Función para registrar calificaciones
def registrar_calificacion(calificaciones):
    nombre_estudiante = input("Ingrese el nombre del estudiante: ")
    calificacion = input("Ingrese la calificación del estudiante: ")
    calificaciones[nombre_estudiante] = calificacion

try:
    with open('calificaciones.json', 'r') as archivo:
        calificaciones = json.load(archivo)
except Exception as err:
    calificaciones = {}
        

while True:
    print("\n1. Agregar alumno y calificacion")
    print("2. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == '1':
        registrar_calificacion(calificaciones)
        print("Calificacion agregada.")
    elif opcion == '2':
        break

with open('calificaciones.json', 'w') as archivo:
    json.dump(calificaciones, archivo, indent=4)