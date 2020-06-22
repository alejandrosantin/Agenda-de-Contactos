## Mostrar el archivo creado anteriormente
def app():
    # with open
    with open('archivo.txt') as archivo:
        for contenido in archivo:
            print(contenido.rstrip()) # rstrip Remueve los saltos de linea



app()