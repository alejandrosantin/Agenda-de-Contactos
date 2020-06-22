cont = 0

print('Bienvenido!\r\n')
pregunta = 'Deseas continuar?\r\n'
preguntar = True

while preguntar == True:

    cont = 0
    pregunta1 = input('2 + 2 es 4?\r\n')

    if pregunta1 == "SI" or pregunta1 == "si":
        cont += 1

    pregunta2 = input('5 + 5 es 8?\r\n')
    if pregunta2 == "NO" or pregunta2 == "no":
        cont += 1

    pregunta3 = input('2 x 2 es 10?\r\n')
    if pregunta3 == "NO" or pregunta3 == "no":
        cont += 1

    print('Tu calificacion es: ', cont)

    if cont == 3:
        print('Felicitaciones eres un genio!')
    else:
        print('Debes repasar')
    
    pregunta += '(Escribe "cerrar" para salir)\r\n'
    pregunta = input(pregunta)
    if pregunta == "cerrar":
        preguntar = False