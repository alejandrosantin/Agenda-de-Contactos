# Constructor
class Restaurant:

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre # Atributo
        self.categoria = categoria
        self.precio = precio # Default: Public, PROTECTED (Se tiene que agregar un guion bajo al inicio del nombre del atributo)
                              # PRIVATE (Doble guion bajo)
    
    # Mostrar la informacion
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}')

    # Getters y Setters
    # Get = Obtiene un valor
    # Set = Modifica un valor
    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

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
    def __init__(self, nombre, categoria, precio, alberca):
        super().__init__(nombre, categoria, precio) # Hago referencia de los que quiero del padre
        self.alberca = alberca

    # Reescribir un metodo es una forma de polimorfismo (Debe llamarse igual)
    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}, Alberca: {self.alberca}')

    # Agregar un metodo que solo exista en Hotel(Es una forma de polimorfismo tambien)
    def get_alberca(self):
        return self.alberca

hotel = Hotel('Hotel POO', '5 Estrellas', 200, 'Si')
hotel.mostrar_informacion()
