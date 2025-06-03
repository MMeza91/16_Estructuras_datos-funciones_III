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


#def modifica_agregado(agregados:list[str]) -> str:
