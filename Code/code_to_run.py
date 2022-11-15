from codigo import Usuario, Pelicula
from time import sleep
user = Usuario()
sw = True
pelicula1 = Pelicula("Duro de matar", ["2:30 PM", "10:10 AM", 
                    "5:00 PM"], 15, 10)
pelicula2 = Pelicula("Buscando a Nemo", ["2:30 PM", "10:10 AM", 
                    "5:00 PM"], 20, 15)
pelicula3 = Pelicula("Avatar", ["2:30 PM", "10:10 AM", 
                    "5:00 PM"], 10, 20)
pelicula1.vaciar_asientos()
pelicula2.vaciar_asientos()
pelicula3.vaciar_asientos()

def menu_peli():
    """
    Despliega las películas disponibles y permite escoger una.
    """
    print(f"Hola, {user.nombre_usuario}, qué quieres ver hoy?")
    print(f"1. {pelicula1.titulo}")
    print(f"2. {pelicula2.titulo}")
    print(f"3. {pelicula3.titulo}")
    opcion = int(input())
    if opcion == 1:
        pelicula1.vender_ticket()
    elif opcion == 2:
        pelicula2.vender_ticket()
    elif opcion == 3:
        pelicula3.vender_ticket()
    else:
        print("Opcion invalida.")
        menu_peli()
    
def menu_inicial():
    """
    Despliega el menú principal y permite elegir una opción.
    """
    print("Bienvenido al teatro.")
    print("Digite una opción:")
    print("1. Ingresar.")
    print("2. Registrarse.")
    print("3. Salir")
    opcion = int(input())
    while(opcion < 1 or opcion > 3):
        print("Bienvenido al teatro.")
        print("Digite una opción:")
        print("1. Ingresar.")
        print("2. Registrarse.")
        print("3. Salir")
        opcion = int(input())
    if opcion == 1:
        if user.sin_usuarios:
            print("Aún no ha creado ningún usuario, ", end="")
            print("regístrese primero.")
            input("Presione enter para volver al menú principal.")
        else:   
            user.ingresar()
            menu_peli()
    elif opcion == 2:
        user.registrar()
    elif opcion == 3:
        print("Adios, hasta pronto.")
        sleep(1)
        exit()
while sw:
    menu_inicial()