from cocina.listar import listar_agregados_elegidos
from cocina.listar import listar_ingredientes_pizzeria
from cocina.listar import listar_masa_o_salsa_elegidos

from cocina.modificar import modifica_masa_o_salsa
#from cocina.modificar import

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
                eleccion=int(input("""\nEscribe el número de tu elección """))
                pregunta=False
            except:
                print("El valor a ingresar debe ser un número entre 1 y 6 incluyendolos.\n")
        
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
            masa_elegida = modifica_masa_o_salsa("Masa",masas)

        elif eleccion == 4:
            salsa_elegida = modifica_masa_o_salsa("Salsa",salsas)

        elif eleccion == 5:
            continue
        elif eleccion == 6:
            eligiendo=pedir_pizza(masa_elegida, salsa_elegida, agregados_elegidos)
        else:
            print("La opción no es válida, debe ser un número entre 1 y 6 incluyendolos.\n")