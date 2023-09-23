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

**IMPORTANTE**: A partir de la siguiente actividad, cada semana tiene su propia rama con las actividades resueltas. Esto se maneja de esta forma, debido a que haremos un proyecto de django repasando todo lo visto en clases y con el manejo de ramas se puede ir viendo el progrreso escalonado delimitado por lo que van solicitando las actividades.

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

Crear un nuevo modelo Paleta con 4 atributos: marca(charfield), modelo(charfield), anio(integerfield), nueva(booleanfield). El modelo debera tener una vista para el formulario de creacion y otra para el listado de paletas creadas (esta ultima debera incluir un formulario de busqueda).

**AVISO**: Los formularios de creacion y busqueda tambien deben crearse en esta actividad.

### Actividad 2: Mejora de templates y panel de admin

Acomodar los templates para que implementen herencia, mitigando la repeticion de codigo. Ademas, acomodar en la barra de navegacion el acceso a las vistas de 'inicio', 'crear_paleta' y 'buscar_paleta'.

### Actividad 3: Apartado admin

Registrar los modelos en el apartado de admin. Luego acceder al mismo y probar crear, modificar, ver, eliminar paletas. Agregar en los modelos registrados el metodo magico `__str__` para que el listado del admin sea mas legible.

## Semana 12

### Actividad 1: Edita y Borra

Al modelo paleta agregarle una vista para la actualizar datos y otra para eliminar paletas. (No utilizar Clases Basadas en Vistas)
En este punto, modificar el nav de la app para que a la vista de creacion se acceda desde la vista de busqueda/listado y el acceso a actualizar o borrar esten en botones junto a cada paleta del listado.

**IMPORTANTE**: Para no requerir validar en la vista de que tipo tiene que ser el parametro que se pasa por la url podemos en la url cuando definimos el nombre del parametro, ejemplo `'paletas/editar/<paleta_id>/'`, indicarle de que tipo queremos que nuestra app detecte que va a ser, ejemplo `'paletas/editar/<int:paleta_id>/'`.

### Actividad 2: CBV

Crear un nuevo modelo PelucheAnimal con 4 atributos: animal(charfield), altura(floatfield), fecha(datefield). El modelo debera contar con una CBV para cada una de las siguientes funcionalidades: crear, listar (incluir el buscador), editar, eliminar y mostrar mas detalles del mismo. No olvidar registrar el modelo en el apartado de admin.  
**IMPORTANTE**: En la CBV del listado se deben encontrar los accesos a todas las demas vistas, esta debe ser la unica accesible desde la barra de navegacion de la pagina.  

**EXTRA**: Podes crear otra app llamada peluche y aca contener todo lo relacionado a PelucheAnimal (y tal vez a futuro sobre peluches en general).

### Actividad 3: Autenticacion

Agregarle al proyecto una nueva app llamada cuentas y luego:

1. Agregar a cuentas un vista para el login (usar un formulario custom que pida el mail ademas de el usuario y la contraseña) y una vista para el logout.
2. Ahora, una vista para que un usuario pueda registrarse en nuestra app.
3. Agregar a las vistas de edicion y borrado de los modelos creados hasta el momento (Paleta y PelucheAnimal) el decorador o mixin, segun corresponda, para limitar el acceso estas funcionalidades a personas que no estan logueadas.

## Semana 13

### Actividad 1: Mas datos

Teniendo en cuenta que pocos son los datos que podemos guardar de un usuario, crea un modelo que este relacionado con User y permita guardar un avatar y algun dato extra sobre el usuario (ej, pagina, biografia, fecha de nacimiento, etc).

### Actividad 2: El perfil

Agregar un apartado donde el usuario pueda ver su informacion (nombre, apellido, avatar, etc) y tambien que tenga un acceso a un apartado para modificar dicha informacion (tambien que se pueda modificar la contraseña).

### Actividad 3: Ver y describir el peluche

Agregarle al peluche animal un atributo para cargarle una imagen y una descripcion (esta permitir que sea con formato de texto enriquecido). Ambos campos deben ser incluidos en todas las vistas relacionadas a peluche animal.
