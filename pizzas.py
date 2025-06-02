
def listar_ingredientes_pizzeria(tipo:str,ingrediente:list[str]):
    """
    Este programa lista los ingredientes de la pizzeria en la terminal, sin devolver valores en return.
    tipo: Masa / Salsa o Ingrediente.
    ingrediente: lista con opciones del tipo.
    """
    print(f"\nEn nuestra pizzeria trabajamos con {len(ingrediente)} tipos de {tipo} para tú pizza:")
    for i in ingrediente:
        print(i)
    print()


def listar_masa_o_salsa_elegidos(tipo:str,elegida:str):
    """
    Este programa lista los ingredientes masa/salsa elegidos en la terminal, sin devolver valores en return.
    tipo: Masa o Salsa.
    elegida: opción elegida por el usuario.
    """
    if elegida == "":
        print(f"Aún debes elegir la {tipo} de tu pizza")
    else:
        print(f"Tienes elegida la {elegida}")


def listar_agregados_elegidos(agregado:list[str]):
    """
    Este programa lista los agregados elegidos en la terminal, sin devolver valores en return.
    agregado: lista con opciones elegidas por el usuario.
    """
    if len(agregado) == 0:
        print("Aún debes elegir los ingredientes de tu pizza")
    else:
        print("Tienes elegidos los siguientes ingredientes:")
        for i in agregado:
            print(i)

def modifica_masa_o_salsa(tipo:str,ingrediente:list[str]) -> str:
    pregunta=True
    while pregunta:
        print(f"¿Que {tipo} deseas elegir?, tenemos:")
        for i in ingrediente:
            print(i)
        respuesta=input("Escriba su elección por favor: ")
        verificador=False
        for i in ingrediente:
            if respuesta.lower() == i.lower():
                pregunta=False
                verificador=True
        if verificador:
            print(f"Su elección es: {respuesta}")
        else:
            print("\nDebe elegir una opción que esté en la lista")
    return respuesta


#def modifica_agregado()
    
def pedir_pizza(masa:str, salsa:str, agregado:list[str]) -> bool:
    """
    se entregan las elecciones del usuario y devuelve el booleano con la respuesta a si se sigue haciendo cambios a la pizza
    """
    print()

    if masa == "":
        print("No ha elegido masa, por defecto se considera Masa Tradicional")
        masa = "Masa Tradicional"
    elif masa != "":
        print(f"La masa elegida es {masa}")

    if salsa == "":
        print("No ha elegido salsa, su pizza se fabricará sin ninguna salsa")
    elif salsa != "":
        print(f"La salsa elegida es {salsa}")

    if len(agregado) == 0:
        print("No ha elegido ingredientes, por defecto se considera Tomate y Aceitunas")
        agregado=["Tomate","Aceitunas"]
    elif len(agregado) != 0:
        print("Los ingredientes elegidos son: ")
        for i in agregado:
            print(i)
    print(f"El tiempo de espera aprox para su pizza es de {20 + 2*len(agregado)} minutos.")

    invalido=True
    while invalido:
        respuesta=input("¿Estas seguro que quieres pedir esta pizza? (si/no)")

        if respuesta.lower() == "s" or respuesta.lower() == "si":
            print("Su pedido ha sido enviado, ¡hasta una próxima oportunidad!")
            invalido=False
            duda=False
        elif respuesta.lower() == "n" or respuesta.lower() == "no":
            invalido=False
            duda=True
        else:
            print("La opción ingresada no es válida\n")
    return duda



masas    = ["Masa Tradicional", "Masa Delgada", "Masa con Bordes de Queso"]
salsas   = ["Salsa de Tomate", "Salsa Alfredo", "Salsa Barbecue", "Salsa Pesto"]
agregados= ["Tomate", "Champiñones", "Aceituna", "Cebolla", "Pollo", "Jamón", "Carne", "Tocino", "Queso"]

print("Bienvenido a Pizza JAT")

"Se inicializan variables"
masa_elegida = ""
salsa_elegida = ""
agregados_elegidos = []

eligiendo=True
while eligiendo:

    print("Elige alguna de las siguientes opciones:")
    print("1.- Conoce los ingredientes de nuestra pizzería.")
    print("2.- Listar ingredientes seleccionados en tú pizza.")
    print("3.- Elige/cambia la masa de la pizza.")
    print("4.- Elige/cambia la salsa de la pizza.")
    print("5.- Elige/cambia los ingredientes en la pizza.")
    print("6.- Pedir a nuestro equipo la pizza elegida.")

    pregunta=True
    while pregunta:
        try:
            eleccion=int(input("Escribe tu elección "))
            pregunta=False
        except:
            print("El valor a ingresar debe ser un número entre 1 y 6 incluyendolos.\n")
    
    if eleccion == 1:
        listar_ingredientes_pizzeria('Masas',masas)
        listar_ingredientes_pizzeria('Salsas',salsas)
        listar_ingredientes_pizzeria('Ingredientes',agregados)

    elif eleccion == 2:
        listar_masa_o_salsa_elegidos("Masa",masa_elegida)
        listar_masa_o_salsa_elegidos("Salsa",salsa_elegida)
        listar_agregados_elegidos(agregados_elegidos)

    elif eleccion == 3:
        masa_elegida = modifica_masa_o_salsa("Masa",masas)

    elif eleccion == 4:
        salsa_elegida = modifica_masa_o_salsa("Salsa",salsas)

    elif eleccion == 5:
        continue
    elif eleccion == 6:
        eligiendo=pedir_pizza(masa_elegida, salsa_elegida, agregados_elegidos)
    else:
        print("La opción no es válida, debe ser un número entre 1 y 6 incluyendolos.\n")