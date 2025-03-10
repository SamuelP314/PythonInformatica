def Cambiar_Asiento(Asientos):
    
    asientos_libres = [int(Asiento) for Asiento, Estado in Asientos.items() if Estado["Estado"] == "Libre"]
   
    while True:
        asiento_elegido = int(input("\n¿Cuál es el número del asiento que quiere cambiar? \n"))
        if asiento_elegido not in asientos_libres and 0 < asiento_elegido <= 10:
            break
        elif asiento_elegido in asientos_libres:
            print("\nSe ha debido de confundir, el asiento introducido está libre. Por favor, intentelo de nuevo.\n")
        else:
            print("\nSe ha debido de confundir, el asiento introducido no existe. Por favor, intentelo de nuevo.\n")