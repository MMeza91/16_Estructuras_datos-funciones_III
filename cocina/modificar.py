

def modifica_masa_o_salsa(tipo:str,ingrediente:list[str], elegido:str) -> str:
    pregunta=True
    while pregunta:
        respuesta="-"
        error=True    
        while error:
            eleccion  = input(f"\n¿Desea elegir una {tipo} diferente? (S/N): ")
            if eleccion.upper() == "S" or eleccion.upper() == "SI":
                error = False
            elif eleccion.upper() == "N" or eleccion.upper() == "NO":
                error = False
                respuesta = elegido
                break
            else: 
                print(f"\nDebe decidir entre elegir una {tipo} diferente [S] o salir [N]")

        
        if respuesta == elegido:
            break;
        else:
            print(f"\n¿Que {tipo} deseas elegir?, tenemos:")
            for i in range(len(ingrediente)):
                print(f"{i+1}.- {ingrediente[i]}")

            error=True    
            while error:
                respuesta = int(input("\nEscriba el número de su elección por favor: "))

                if respuesta > 0 or respuesta <= len(ingrediente):
                    error = False
                else: 
                    print(f"El valor ingresado no corresponde debe ser un valor entre 1 y {len(ingrediente)}")
            
            for i in range(len(ingrediente)):
                if respuesta == (i+1):
                    respuesta = ingrediente[i]
                    print(ingrediente[i])
            print(f"\nSu elección es: {respuesta}\n")
        pregunta = False
      
    return respuesta


def modifica_agregado(agregados:list[str], ingredientes:list[str]) -> list[str]:

    """
    Permite modificar ingredientes de la pizza.

    agregados: lista de ingredientes agregadas por el usuario a la pizza.
    ingredientes: lista de ingredientes a disposición en la tienda.
    """
    
    pregunta = True
    while pregunta:

        print("\nLos ingredientes que tienes elegidos hasta el momento son:")
        for i in range(len(agregados)):
            print(f"{i+1}.- {agregados[i]}")

        print("\nLos ingredientes que puedes agregar son:")
        for i in range(len(ingredientes)):
            if not ingredientes[i] in agregados:
                print(f"{i+1}.- {ingredientes[i]}")

        error=True
        while error:
            if len(agregados) == 0:
                accion = input("\n¿Desea agregar [A] un ingediente en su pizza? [\"S\" para salir]: ")
            else: 
                accion = input("\n¿Desea modificar [M] o agregar [A] un ingediente en su pizza? [\"S\" para salir]: ")
            
            if accion.upper() == "M" or accion.upper() =="MODIFICAR":

                error=True
                while error:
                    modificado = int(input("Ingrese el número de ingrediente en su lista a modificar: "))

                    if modificado > 0 and modificado <= len(agregados):
                        error = False
                    else: 
                        print(f"El valor ingresado no corresponde debe ser un valor entre 1 y {len(agregados)}")

                error=True    
                while error:
                    ingrediente_nuevo = int(input("Ingrese el número de ingrediente de nuestra tienda a agregar: "))
                    if ingrediente_nuevo > 0 and ingrediente_nuevo <= len(ingredientes):
                        error = False
                    else: 
                        print(f"El valor ingresado no corresponde debe ser un valor entre 1 y {len(agregados)}")
                
                agregados[modificado - 1] = ingredientes[ingrediente_nuevo -1]


            elif accion.upper() == "A" or accion.upper() =="AGREGAR":
                error=True    
                while error:
                    ingrediente_nuevo = int(input("Ingrese el número de ingrediente de nuestra tienda a agregar: "))
                    if ingrediente_nuevo > 0 and ingrediente_nuevo <= len(ingredientes):
                        error = False
                    else: 
                        print(f"El valor ingresado no corresponde debe ser un valor entre 0 y {len(agregados)}")
                
                agregados.append(ingredientes[ingrediente_nuevo -1])

            
            elif accion.upper() == "S" or accion.upper() =="SALIR":
                error = False
                pregunta = False


            else:
                print("""\nEl valor ingresado no es válido
    Escriba \"A\" para AGREGAR un nuevo ingrediente
    Escriba \"M\" para MODIGICAR un un ingrediente de la lista (En caso de ya tener ingredientes seleccionados)
    Escriba \"S\" para salir de la sección\n
                  """)

        

        
    return agregados
