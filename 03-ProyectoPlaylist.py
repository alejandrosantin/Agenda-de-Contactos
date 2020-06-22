playlist = {} # Diccionario vacio
playlist['canciones'] = [] # lista vacia de canciones

# Funcion principal
def app():
    
    

    # Agregar playlist
    agregar_playlist = True

    while agregar_playlist:
        nombre_playlist = input('¿Como deseas nombrar la playlist?\r\n')
        
        if nombre_playlist:
            playlist['nombre'] = nombre_playlist

        # Ya tenemos un nombre, desacticar el True

        agregar_playlist = False

        print(playlist)

        agregar_canciones()


# Funcion para agregar canciones
def agregar_canciones():
    # Bandera para agregar canciones
    agregar_cancion = True
    while agregar_cancion:
        # Preguntar al usuario que cancion desea agregar
        nombre_playlist = playlist['nombre']
        pregunta = f'\r\nAgrega canciones para la playlist {nombre_playlist}: \r\n'
        pregunta += 'Escribe "X" para dejar de agregar canciones\r\n'
        cancion = input(pregunta)
        if cancion == 'X' or cancion == 'x':
            # Dejar de agregar canciones
            print('Finalizando...\r\n')
            agregar_cancion = False

            # Funcion para mostrar resumen de la playlist
            mostrar_resumen()
        else:
             playlist['canciones'].append(cancion)
             print(playlist)

def mostrar_resumen():
    nombre_playlist = playlist['nombre']
    print(f'Playlist: {nombre_playlist} \r\n')
    print('Canciones:\r\n')
    for cancion in playlist['canciones']:
        print(cancion)
        print(' ')


       
   


app()