# Constructor
class Restaurant:

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre # Atributo
        self.categoria = categoria
        self.__precio = precio # Default: Public, PROTECTED (Se tiene que agregar un guion bajo al inicio del nombre del atributo)
                              # PRIVATE (Doble guion bajo)
    
    # Mostrar la informacion
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.__precio}')

    # Getters y Setters
    # Get = Obtiene un valor
    # Set = Modifica un valor
    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio

# Instanciar la clase
restaurant = Restaurant('Pizzeria', 'Pizzas', 120)

print(restaurant)
restaurant.mostrar_informacion()


restaurant2 = Restaurant('Viejo Dave', 'Hamburguesas', 260)
restaurant2.mostrar_informacion()

restaurant.set_precio(900)
precio = restaurant.get_precio()
print(precio)
restaurant2.set_precio(1222222222)
precio2 = restaurant2.get_precio()
print(precio2)  

# Crear una clase hijo de Restaurant
class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio):
        super().__init__(nombre, categoria, precio)

hotel = Hotel('Hotel POO', '5 Estrellas', 200)
hotel.mostrar_informacion()