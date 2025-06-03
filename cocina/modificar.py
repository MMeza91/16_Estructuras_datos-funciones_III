

def modifica_masa_o_salsa(tipo:str,ingrediente:list[str]) -> str:
    pregunta=True
    while pregunta:
        print(f"\n¿Que {tipo} deseas elegir?, tenemos:")
        for i in range(len(ingrediente)):
            print(f"{i+1}.- {ingrediente[i]}")

        respuesta  = int(input("\nEscriba el numero de su elección por favor: "))
        if respuesta >=1 or respuesta <= len(ingrediente):
            for i in range(len(ingrediente)):
                if respuesta == (i+1):
                    respuesta = ingrediente[i]
                    print(ingrediente[i])
            print(f"\nSu elección es: {respuesta}\n")
            pregunta = False
        else:
            print("\nDebe ser el numero de una opción que esté en la lista")
    return respuesta


def modifica_agregado(agregados:list[str], ingredientes:list[str]) -> list[str]:
    
    pregunta = True
    while pregunta:

        print("\nLos ingredientes que tienes elegidos hasta el momento son:")
        for i in range(len(agregados)):
            print(f"{i+1}.- {agregados[i]}")

        print("\nLos ingredientes que puedes agregar son:")
        for i in range(len(ingredientes)):
            if not ingredientes[i] in agregados:
                print(f"{i+1}.- {ingredientes[i]}")


        accion = input("\n¿Desea modificar o agregar un ingediente en su pizza? (M/A) [\"S\" para salir]: ")

        if accion.upper() == "M" or accion.upper() =="MODIFICAR":
            error=True
            while error:
                modificado = int(input("Ingrese el número de ingrediente en su lista a modificar: "))
                if modificado > 0 or modificado <= len(agregados)
                    error = False
                else: 
                    print(f"El valor ingresado no corresponde debe ser un valor entre 0 y {len(agregados)}")

            error=True    
            while error:
                ingrediente_nuevo = int(input("Ingrese el número de ingrediente de nuestra tienda a agregar: "))
                if ingrediente_nuevo > 0 or ingrediente_nuevo <= len(ingrediente_nuevo)
                    error = False
                else: 
                    print(f"El valor ingresado no corresponde debe ser un valor entre 0 y {len(agregados)}")
            
            agregados[modificado - 1] = ingredientes[ingrediente_nuevo -1]


        elif accion.upper() == "A" or accion.upper() =="AGREGAR":
            error=True    
            while error:
                ingrediente_nuevo = int(input("Ingrese el número de ingrediente de nuestra tienda a agregar: "))
                if ingrediente_nuevo > 0 or ingrediente_nuevo <= len(ingrediente_nuevo)
                    error = False
                else: 
                    print(f"El valor ingresado no corresponde debe ser un valor entre 0 y {len(agregados)}")
            
            agregados.append(ingredientes[ingrediente_nuevo -1])

        
        elif accion.upper() == "S" or accion.upper() =="SALIR":
 
            break;

        else:
            print("""\nEl valor ingresado no es válido
                  Escriba \"A\" para AGREGAR un nuevo ingrediente
                  Escriba \"M\" para MODIGICAR un un ingrediente de la lista
                  Escriba \"S\" para salir de la sección\n
                  """)
    return agregados
