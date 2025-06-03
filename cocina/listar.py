def listar_ingredientes_pizzeria(tipo:str,ingrediente:list[str]):
    """
    Este programa lista los ingredientes de la pizzeria en la terminal, sin devolver valores en return.
    tipo: Masa / Salsa o Ingrediente.
    ingrediente: lista con opciones del tipo.
    """
    print(f"\nEn nuestra pizzeria trabajamos con {len(ingrediente)} tipos de {tipo} para tú pizza:")
    for i in range(len(ingrediente)):
        print(f"{i+1}.- {ingrediente[i]}")
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
        for i in range(len(agregado)):
            print(f"{i+1}.- {agregado[i]}")