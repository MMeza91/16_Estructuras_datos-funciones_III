def pedir_pizza(masa:str, salsa:str, agregado:list[str]) -> bool:
    """
    se entregan las elecciones del usuario y devuelve el booleano con la respuesta a si se sigue haciendo cambios a la pizza
    """
    print()

    if masa == "":
        print("No ha elegido masa, por defecto se considera \"Masa Tradicional\"")
        masa = "Masa Tradicional"
    elif masa != "":
        print(f"La masa elegida es {masa}")

    if salsa == "":
        print("No ha elegido salsa, su pizza se fabricará sin ninguna salsa")
    elif salsa != "":
        print(f"La salsa elegida es {salsa}")
    
    print("Los ingredientes elegidos son: ")
    for i in range(len(agregado)):
        print(f"{i+1}.- {agregado[i]}")

    print(f"El tiempo de espera aprox para su pizza es de {20 + 2*len(agregado)} minutos.")

    invalido = True
    while invalido:
        respuesta = input("¿Estas seguro que quieres pedir esta pizza? (si/no) <")

        if respuesta.lower() == "s" or respuesta.lower() == "si":
            print("Su pedido ha sido enviado, ¡hasta una próxima oportunidad!")
            invalido = False
            duda = False
        elif respuesta.lower() == "n" or respuesta.lower() == "no":
            invalido = False
            duda = True
        else:
            print("La opción ingresada no es válida\n")
    return duda