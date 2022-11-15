class Usuario():
    def __init__(self) -> None:
        self.nombre_usuario = str
        self.contraseña = str
        self.usuarios = []
        self.password = []
        self.preferencia = int
    
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
        print("Digite el número de asiento de su preferencia.")
        self.preferencia = input()
        print("¡Registro exitoso!")
        input("Presione enter.")
        
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
                    

class Asiento():
    def __init__(self) -> None:
        self.asientos = []
        
class Tickete():
    def __init__(self) -> None:
        self.regular = int
        self.vip = int
        self.cantidad = int
        self.disponibles = int
        self.tipo = int
                
class Pelicula(Tickete, Asiento):
    def __init__(self, titulo: str, hora: str, regular: int,
                 vip: int) -> None:
        self.titulo = titulo
        self.hora = hora
        self.regular = regular
        self.vip = vip
        self.cantidad = self.regular + self.vip
        self.disponibles = self.cantidad
    
    def vender_ticket(self) -> None:
        print("Digite el tipo de entrada que desea comprar.")
        print("Digite 1 para regular o 2 para VIP")
        self.tipo = int(input)
        numero_tickets = int(input("Por favor digite la cantidad \
            de entradas que desea comprar."))
        if numero_tickets <= self.disponibles:
            self.disponibles -= numero_tickets
            print("Compra realizada.")
        else: 
            print(f"Lo sentimos, no hay esa cantidad de entradas \
                disponibles. Quedan {numero_tickets} entradas")
            while numero_tickets > self.disponibles:
                numero_tickets = int(input("Por favor digite la \
                    cantidad de entradas que desea comprar."))
            self.disponibles -= numero_tickets
        print("Escoja los asientos que desee:")  
        self.escoger_asiento(numero_tickets)  
        print("Compra realizada.")
        
    def escoger_asiento(self, comprados) -> None:
        aux = 0
        num_asiento = int
        while(aux < comprados):
            print("Digite un número de tickete:")
            if num_asiento in self.asientos:
                for j in range(self.asientos):
                    if self.asientos[j] == num_asiento:
                        self.num_asiento[j] = 0
                        aux += 1
            else:
                print("Asiento no disponible.")
            
    
    def vaciar_acientos(self) -> None:
        for i in range(self.cantidad):
            self.asientos.append(i+1)