from time import sleep
class Usuario():
    def __init__(self) -> None:
        self.nombre_usuario = str
        self.contraseña = str
        self.usuarios = []
        self.password = []
        self.preferencia = int
        self.sin_usuarios = True
    
    def registrar(self) -> None:
        """
        Permite que los usuarios registrados puedan ingresar.
        """
        print("¡Hola, bienvenido a registro!")
        print("Por favor, digite un nombre de usuario:")
        self.nombre_usuario = input()
        if self.nombre_usuario in self.usuarios:
            while self.nombre_usuario in self.usuarios:
                print("Digite otro nombre, este ya existe:")
                self.nombre_usuario = input()
            self.usuarios.append(self.nombre_usuario)
        else:
            self.usuarios.append(self.nombre_usuario)
        print("Por favor, digite una contraseña:")
        self.contraseña = input()
        self.password.append(self.contraseña)
        print("Digite el número de asiento de su preferencia.")
        self.preferencia = input()
        print("¡Registro exitoso!")
        self.sin_usuarios = False
        input("Presione enter para continuar.")
        
    def ingresar(self) -> None:
        """
        Permite crear uno o más usuarios.
        """
        print("¡Hola, bienvenido a ingreso!")
        print("Por favor, digite su nombre de usuario:")
        self.nombre_usuario = input()
        while self.nombre_usuario not in self.usuarios:
            print("No existe este nombre de usuario, por favor \
                digite otro:")
            self.nombre_usuario = input()
        if self.nombre_usuario in self.usuarios:
            print("Por favor, digite una contraseña:")
            self.contraseña = input()
        if self.contraseña in self.password:
            print("¡Ingreso exitoso!")
            sleep(1.3)
        else:
            while self.contraseña not in self.password:
                print("Contraseña incorrecta, intenta de nuevo")
                self.contraseña = input()
            if self.contraseña in self.password:
                print("¡Ingreso exitoso!")
                sleep(1.3)

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
    def __init__(self, titulo: str, hora: list, regular: int,
                 vip: int) -> None:
        self.titulo = titulo
        self.hora = hora
        self.regular = regular
        self.vip = vip
        self.cantidad = self.regular + self.vip
        self.disponibles = self.cantidad
        self.asientos = []
    
    def vender_ticket(self) -> None:
        """
        Este método permite que el usuario adquiera sus entradas.
        """
        print("Escoja un horario.")
        print(f"1. {self.hora[0]}")
        print(f"2. {self.hora[1]}")
        print(f"3. {self.hora[1]}")
        horario = input()
        print("Digite el tipo de entrada que desea comprar.")
        print("Digite 1 para regular o 2 para VIP")
        self.tipo = int(input())
        print("Por favor digite la cantidad " +
            "de entradas que desea comprar.")
        numero_tickets = int(input())
        if numero_tickets <= self.disponibles:
            self.disponibles -= numero_tickets
        else: 
            print("Lo sentimos, no hay esa cantidad de entradas " +
                f"disponibles. Quedan {numero_tickets} entradas")
            while numero_tickets > self.disponibles:
                numero_tickets = int(input("Por favor digite la " +
                    "cantidad de entradas que desea comprar."))
            self.disponibles -= numero_tickets
            if self.tipo == 1:
                self.regular -= 1
            elif self.tipo == 2:
                self.vip -= 1
        print("Escoja los asientos que desee:")  
        self.escoger_asiento(numero_tickets)  
        print("Compra realizada.")
        sleep(1)
        print("Disfrute la película.")
        sleep(1)
        
    def escoger_asiento(self, comprados) -> None:
        """
        Permite que el usuario escoja los asientos de su preferencia.
        """
        aux = 0
        num_asiento = int
        while(aux < comprados):
            print("Digite un número de asiento:")
            num_asiento = int(input())
            if num_asiento in self.asientos:
                for j in range(len(self.asientos)):
                    if self.asientos[j] == num_asiento:
                        self.asientos[j] = 0
                        aux += 1
            else:
                print("Asiento no disponible.")
            
    
    def vaciar_acientos(self) -> None:
        """
        Permite que todos los puestos estén disponibles.
        """
        for i in range(self.cantidad):
            self.asientos.append(i+1)