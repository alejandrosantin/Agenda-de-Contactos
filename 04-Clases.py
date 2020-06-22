class Restaurant:

    def agregar_restaurant(self, nombre):
        self.nombre = nombre # Atributo
    
    # Mostrar la informacion
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}')

# Instanciar la clase
restaurant = Restaurant()

print(restaurant)
restaurant.agregar_restaurant('Pizzeria')
restaurant.mostrar_informacion()

restaurant2 = Restaurant()
restaurant2.agregar_restaurant('Viejo Dave')
restaurant2.mostrar_informacion()

# Mostrar la informacion accediendo por fuera
print(f'Nombre Restaurant2: {restaurant2.nombre}')