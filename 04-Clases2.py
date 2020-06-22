# Constructor
class Restaurant:

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre # Atributo
        self.categoria = categoria
        self.precio = precio
    
    # Mostrar la informacion
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}')

# Instanciar la clase
restaurant = Restaurant('Pizzeria', 'Pizzas', 120)

print(restaurant)
restaurant.mostrar_informacion()


restaurant2 = Restaurant('Viejo Dave', 'Hamburguesas', 260)
restaurant2.mostrar_informacion()