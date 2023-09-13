'''
### Registrando gastos

Escribe un programa en Python que permita a un usuario registrar sus gastos diarios en un 
archivo de texto llamado "gastos.txt". El programa debe permitir al usuario ingresar la descripción 
del gasto y la cantidad gastada. Luego, debe guardar estos datos en el archivo en el siguiente formato:

"Fecha: {fecha} - Descripción: {descripción} - Cantidad: {cantidad}"

Donde fecha es la fecha actual y descripción y cantidad son los datos ingresados por el usuario.
'''


import datetime

# Función para registrar gastos
def registrar_gasto():
    fecha = datetime.date.today()
    descripcion = input("Ingrese la descripción del gasto: ")
    cantidad = input("Ingrese la cantidad gastada: ")

    with open("gastos.txt", "a") as archivo:
        archivo.write(f"Fecha: {fecha} - Descripción: {descripcion} - Cantidad: {cantidad}\n")

# Llamada a la función para registrar un gasto
registrar_gasto()