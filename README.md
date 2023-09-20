# Actividades de repaso

## Semana 1

- **Actividad 1**: Calculadora base
- **Actividad 2**: Los caracteres ultimos rien mejor
- **Actividad 3**: Cambio manual
- **Actividad 4**: Cuanto y donde?

## Semana 2

- **Actividad 1**: Nombres unicos
- **Actividad 2**: Actualizando la tienda
- **Actividad 3**: Python uno, Python dos, Python 3...
- **Actividad 4**: Intersectando y uniendo

## Semana 3

- **Actividad 1**: Paresitos
- **Actividad 2**: x 3, x 5
- **Actividad 3**: Positivo! Par si o Par no?
- **Actividad 4**: Alineando la condicional

## Semana 4

- **Actividad 1**: Hay tabla
- **Actividad 2**: Ubica la palabra
- **Actividad 3**: Vocales perdidas?
- **Actividad 4**: Salteando palabras

## Semana 5

- **Actividad 1**: Gestión de Tareas Pendientes
- **Actividad 2**: Contactame
- **Actividad 3**: Gestión de Tareas Pendientes
- **Actividad 4**: Tu promedio

## Semana 6

- **Actividad 1**: Búsqueda del error
- **Actividad 2**: Edad correcta
- **Actividad 3**: Estamos de oferta

## Semana 7

- **Actividad 1**: Figuras
- **Actividad 2**: Calculadora POO
- **Actividad 3**: Gestion de empleados
- **Actividad 4**: La Biblioteca
- **Actividad 5**: Tienda en Línea

## Semana 8

- **Actividad 1**: Registrando gastos
- **Actividad 2**: Gestión de Tareas Pendientes (Con persistencia de datos)
- **Actividad 3**: Registro de calificaciones
- **Actividad 4**: Metiendo a la bolsa

## Semana 9

### Actividad 1: Repasemos Git

Sigamos las siguientes instrucciones para practicar un poco el uso de git…

1. Crea una carpeta nueva y abrirla para trabajar en ella.
2. Inicializa un repositorio de git.
3. Crea una rama por cada semana, hasta la semana 8 inclusive, de ejercicios en esta guia (semana1, semana2, semana3, etc).
4. Por cada rama de las semanas seguir los siguientes pasos:
    1. Crear una carpeta con el nombre de la rama.
    2. Dentro de la carpeta crear para la actividad 1 un archivo que contenga la resolucion y luego hacer un commit con el mensaje “Actividad 1”.
    3. Repetir el punto anterior para las actividades restantes.
5. Luego, volver a la rama principal (master o main, depende como lo tengan configurado) y hacer un merge por cada una de las ramas de las semanas.
6. Por ultimo, hacer un push a un repositorio creado en github.

Con esto dejaremos todo lo que tenia cada rama (cada carpeta de actividades) en la rama principal.

### Actividad 2: Repaso creacion de proyecto

Crear un proyecto de Django siguiendo los pasos vistos en clase.
Este proyecto debera contar con 2 vistas:

1. La primera debera enviar por HttpResponse un string que indique en que año aproximadamente nacio una persona si le pasamos por la url la edad (para revisar si un string es solo numerico se puede usar el metodo .isnumeric() de los strings que devuelve True en caso de que sean solo numeros).
2. La segunda solo requerira que en lugar de pasarle un string como argumento al HttpResponse se le pase un template en el cual se mostrara un mensaje que diga "Bienvenidos".
La url de acceso debera ser 'bienvenida/'.

## Semana 10

### Actividad 1: Trabajemos con apps

A partir de este punto las actividades siguientes se centraran en la modificacion y mejora del proyecto que se arranco en la actividad 2 de la semana 9.
Teniendo esto en cuenta, realizar las siguientes modificaciones:

1. Crear una app 'inicio' a la cual le trasladaremos las vistas creadas en la actividad pasada. Recordar modificar el setting.py para que nuestro proyecto reconozca la app creada. (una vez trasladadas las vistas eliminar el archivo views.py que quedo vacio)
2. Generar el archivo urls.py para nuestra app y agregar el codigo correspondiente en el urls.py que se encuentra con el settings.py para que se conecte al urls.py de nuestra app ( uso de la funcionalidad "include" ).
3. Cambiar la carga actual de templates en las vistas por el uso de render (el shortcut). Cambiar la ubicacion de los templates para que esten dentro de la app que le corresponda.

### Actividad 2: Usemos un template predefinido

Buscar en [starbootstrap](https://startbootstrap.com/?showAngular=false&showPro=false&showVue=false) un template que te guste, descargalo e implementalo (con los cambios que sientas necesario en el html) en el proyecto en una vista llamada inicio dentro de la app inicio. Para esta vista definir el path de la url vacio.

### Actividad 3: Guardo y muestro

1. Crear un modelo que cuente con 3 atributos: nombre(charfield), edad(integerfield) y fecha(datefield). Para este modelo agregaremos una vista que tome por url 2 parametros, uno para el charfield, otro para el integerfield y el datefield lo rellenaremos con la fecha del momento cuando se crea. Teniendo estos datos en la vista generaremos un objeto para guardarlo en la base de datos y, tambien, para pasarlo por contexto a un template que crearemos.
2. El template del punto anterior debera mostrar nombre y edad. Ademas, en caso que el dia del campo fecha sea mayor a 15 se debera mostrar en un listado cada letra del nombre.

**Recordatorio**: Una vez creado un modelo ejecutar el comando makemigrations y luego migrate para que se plasme la creacion del modelo en la bd.

## Semana 11

### Actividad 1: Formularios y listado

Crear un nuevo modelo Paleta (atributos: marca, modelo, anio, nueva), el cual debera tener una vista para el formulario de creacion y otra para el listado de paletas creadas (esta ultima debera incluir un formulario de busqueda).

**AVISO**: Los formularios de creacion y busqueda tambien deben crearse en esta actividad. El atributo nueva debera ser un BooleanField.

### Actividad 2: Mejora de templates y panel de admin

Acomodar los templates para que implementen herencia, mitigando la repeticion de codigo. Ademas, acomodar en la barra de navegacion el acceso a las vistas de 'inicio', 'crear_paleta' y 'buscar_paleta'.

### Actividad 3: Apartado admin

Registrar los modelos en el apartado de admin. Luego acceder al mismo y probar crear, modificar, ver, eliminar paletas. Agregar en los modelos registrados el metodo magico `__str__` para que el listado del admin sea mas legible.
