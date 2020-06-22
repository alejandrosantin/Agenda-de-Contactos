def app():
    # Crear el archivo
    archivo = open('archivo.txt', 'w') # w es archivo de escritura, si no existe lo creará

    # Generar numeros en archivo
    for i in range(0, 20):
        archivo.write('Esta es la linea ' + str(i) + "\r\n")

    # Es buena practica siempre que se utiliza open cerrar el archivo
    archivo.close()

app()