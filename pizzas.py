from cocina.listar import listar_agregados_elegidos
from cocina.listar import listar_ingredientes_pizzeria
from cocina.listar import listar_masa_o_salsa_elegidos

from cocina.modificar import modifica_masa_o_salsa
from cocina.modificar import modifica_agregado

from cocina.pedir import pedir_pizza

#Se agregan lista de ingredientes que pueden ser modificados sin alterar el programa

masas    = ["Masa Tradicional", "Masa Delgada", "Masa con Bordes de Queso"]
salsas   = ["Salsa de Tomate", "Salsa Alfredo", "Salsa Barbecue", "Salsa Pesto"]
agregados= ["Tomate", "Champiñones", "Aceituna", "Cebolla", "Pollo", "Jamón", "Carne", "Tocino", "Queso"]

if __name__ == "__main__":

    print("\n\n\nBienvenido a Pizza JAT\n\n\n")

    "Se inicializan variables"
    masa_elegida = ""
    salsa_elegida = ""
    agregados_elegidos = []

    eligiendo=True
    while eligiendo:

        print("""\nElige alguna de las siguientes opciones:
    1.- Conoce los ingredientes de nuestra pizzería.
    2.- Listar ingredientes seleccionados en tú pizza.
    3.- Elige/cambia la masa de la pizza.
    4.- Elige/cambia la salsa de la pizza.
    5.- Elige/cambia los ingredientes en la pizza.
    6.- Pedir a nuestro equipo la pizza elegida.
    7.- Salir del programa.
            
              """)

        pregunta=True
        while pregunta:
            try:
                eleccion=int(input("""\nEscribe el número de tu elección """))
                pregunta=False
            except:
                print("El valor a ingresar debe ser un número entre 1 y 7 incluyendolos.\n")
        
        if eleccion == 1:
            listar_ingredientes_pizzeria('Masas',masas)
            listar_ingredientes_pizzeria('Salsas',salsas)
            listar_ingredientes_pizzeria('Ingredientes',agregados)

        elif eleccion == 2:
            print()
            listar_masa_o_salsa_elegidos("Masa",masa_elegida)
            listar_masa_o_salsa_elegidos("Salsa",salsa_elegida)
            listar_agregados_elegidos(agregados_elegidos)
            print()

        elif eleccion == 3:
            masa_elegida = modifica_masa_o_salsa("Masa",masas,masa_elegida)

        elif eleccion == 4:
            salsa_elegida = modifica_masa_o_salsa("Salsa",salsas,salsa_elegida)

        elif eleccion == 5:
            masa_elegida = modifica_agregado(agregados_elegidos, agregados)

        elif eleccion == 6:
            opcion=True
            if masa_elegida=="":
                print("\nAun debe elegir el tipo de masa")
                opcion=False
            if salsa_elegida=="":
                print("\nAun debe elegir el tipo de salsa")
                opcion=False
            if len(agregados_elegidos) == 0:
                print("\nAun debe elegir los ingredientes")
                opcion=False

            if opcion:            
                eligiendo=pedir_pizza(masa_elegida, salsa_elegida, agregados_elegidos)

        elif eleccion == 7:
            print("Nos vemos para tu próxima pizza, ¡adios!")
            break;

        else:
            print("La opción no es válida, debe ser un número entre 1 y 7 incluyendolos.\n")