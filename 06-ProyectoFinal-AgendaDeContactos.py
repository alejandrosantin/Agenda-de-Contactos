import os

CARPETA = 'Contactos/' # Va en mayusculas xq asi da a entender que es una constante, es decir, no debe ser modificada
EXTENSION = '.txt' # Extension de archivos

#Contactos
class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

def app():
    #Revisa si la carpeta ya esta creada
    crear_directorio()

    #Muestra el menu de opciones
    mostrar_menu()

    #Preguntar al usuario la accion a realizar
    preguntar = True
    while preguntar:
        opcion = input('Seleccione una opción: \r\n')
        opcion = int(opcion)

    #Ejecutar las opciones (¡Switch no existe en python!)
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contactos()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        else:
            print('Opcion no válida, intente de nuevo')

def eliminar_contacto():
    nombre = input('Seleccione el contacto que desea eliminar: \r\n')
    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('Contacto eliminado correctamente')
    except:
        print('No existe ese contacto\r\n')

    #Reiniciar la pp
    app()
    
def buscar_contacto():
    nombre = input('Seleccione el contacto que desea buscar: \r\n')

    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('\r\n Informacion del contacto: \r\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    except IOError:
        print('El archivo no existe')
        print(IOError)

    #Reiniciar la app
    app()

def mostrar_contactos():
    archivos = os.listdir(CARPETA)

    # Recorre el iterador pero unicamente si termina en la extension .txt
    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]

    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                #Imprime los contenidos
                print(linea.rstrip())
            #Imprime un separador entre contactos
            print('\r\n')



def editar_contacto():
    print('Escribe el nombre del contacto que desea editar\r\n')
    nombre_anterior = input('Nombre del contacto que desea editar: \r\n')
    # Revisar si el archivo existe
    existe = existe_contacto(nombre_anterior)

    if existe:
        with open(CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:

            # Resto de los campos
            nombre_contacto = input('Agrega el nuevo nombre: \r\n')
            telefono_contacto = input('Agrega el nuevo Telefono: \r\n')
            categoria_contacto = input('Agrega la nueva Categoria: \r\n')

            # Instanciar
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            # Escribir en el archivo
            archivo.write('Nombre: ' + contacto.nombre + '\r\n')
            archivo.write('Telefono: ' + contacto.telefono + '\r\n')
            archivo.write('Categoria: ' + contacto.categoria + '\r\n')  

            # Renombrar el archivo 
            os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)

            #Mensaje de exito
            print('\r\nContacto Editado Correctamente \r\n')

            # Reiniciar la applicacion
        app()


    else:
        print('Ese contacto no existe\r\n')

    # Reiniciar la applicacion
    app()


def agregar_contacto():
    print('Escribe los datos para agregar el nuevo contacto')
    nombre_contacto = input('Nombre del Contacto: \r\n')
    
    # Revisar si el archivo ya existe antes de crearlo
    existe = existe_contacto(nombre_contacto)

    if not existe:
            with open(CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:
                 # Resto de los campos
                telefono_contacto = input('Agrega el Telefono: \r\n')
                categoria_contacto = input('Categoria Contacto: \r\n')

                # Instanciar la clase
                contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

                # Escribir en el archivo
                archivo.write('Nombre: ' + contacto.nombre + '\r\n')
                archivo.write('Telefono: ' + contacto.telefono + '\r\n')
                archivo.write('Categoria: ' + contacto.categoria + '\r\n')   

                # Mostrar un mensaje de exito
                print('\r\nContaco Creado Correctamente \r\n')

    else:
        print('\r\nEse contacto ya existe\r\n')

    # Reiniciar la app
    app()


def mostrar_menu():
    print('Seleccione lo que desea hacer:')
    print('1) Agregar Nuevo Contacto')
    print('2) Editar Contacto')
    print('3) Ver Contactos')
    print('4) Buscar Contacto')
    print('5) Eliminar Contacto')



def crear_directorio():
    if not os.path.exists('Contactos/'):  # Si la carpeta no existe entonces crear la carpeta
        #Crear la carpeta
        os.makedirs('Contactos/')


def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)


        
app()