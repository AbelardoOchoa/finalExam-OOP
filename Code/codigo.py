class Usuario():
    def __init__(self) -> None:
        self.nombre_usuario = str
        self.contraseña = str
        self.usuarios = []
        self.password = []
    
    def registrar(self) -> None:
        print("¡Hola, bienvenido a registro!")
        print("Por favor, digite un nombre de usuario:")
        self.nombre_usuario = input()
        if self.nombre_usuario in self.usuarios:
            while self.nombre_usuario in self.usuarios:
                print("Digite otro nombre, este ya existe.")
            self.usuarios.append(self.nombre_usuario)
        else:
            self.usuarios.append(self.nombre_usuario)
        print("Por favor, digite una contraseña:")
        self.contraseña = input()
        self.nombre_usuario = input()
        
    def ingresar(self) -> None:
        print("¡Hola, bienvenido a ingreso!")
        print("Por favor, digite su nombre de usuario:")
        self.nombre_usuario = input()
        if self.nombre_usuario in self.usuarios:
            print("Por favor, digite una contraseña:")
            self.contraseña = input()
            if self.contraseña in self.password:
                print("¡Ingreso exitoso!")
            else:
                while self.contraseña not in self.password:
                    print("Contraseña incorrecta, intenta de nuevo")
                    self.contraseña = input()
                    
        

class Pelicula():
    def __init__(self, titulo: str, duracion: str) -> None:
        self.titulo = titulo
        self.duracion = duracion

class Asiento():
    def __init__(self) -> None:
        self.asientos = []
        self.disponibles = int
        
class Tickete():
    def __init__(self, cantidad: int) -> None:
        self.cantidad = cantidad
        self.disponibles = self.cantidad
        self.tipo = int
    
    def vender_ticket(self) -> None:
        print("Digite el tipo de entrada que desea comprar.")
        print("Digite 1 para regular o 2 para VIP")
        self.tipo = int(input)
        numero_tickets = int(input("Por favor digite la cantidad de entradas \
            que desea comprar."))
        if numero_tickets <= self.disponibles:
            self.disponibles -= numero_tickets
            print("Compra realizada.")
        else: 
            print(f"Lo sentimos, no hay esa cantidad de entradas \
                disponibles. Quedan {numero_tickets} entradas")
            while numero_tickets > self.disponibles:
                numero_tickets = int(input("Por favor digite la cantidad \
                    de entradas que desea comprar."))
            self.disponibles -= numero_tickets
            print("Compra realizada.")
                
        

class Vip(Tickete):
    pass

class Regular(Tickete):
    pass