def Cambiar_Asiento(Asientos):
    
    asientos_libres=[]
    
    for Asiento, Estado in Asientos.items():
       if Estado["Estado"] == "Libre":
           asientos_libres.append(int(Asiento))
   
    while True:
        asiento_elegido = int(input("\n¿Cuál es el número del asiento que quiere cambiar? \n"))
        if asiento_elegido not in asientos_libres and 0 < asiento_elegido <= 10:
            break
        elif asiento_elegido in asientos_libres:
            print("\nSe ha debido de confundir, el asiento introducido está libre. Por favor, intentelo de nuevo.\n")
        else:
            print("\nSe ha debido de confundir, el asiento introducido no existe. Por favor, intentelo de nuevo.\n")


    while True:
        nombre = input("\nPor motivos de seguridad, necesitamos el nombre al que se puso la reserva. \n")
        if Asientos[asiento_elegido]["Nombre"] == nombre:
            Asientos[asiento_elegido]["Estado"] = "Libre"
            Asientos[asiento_elegido]["Nombre"] = ""
            asientos_libres.append(asiento_elegido)
            asientos_libres.sort()
            print("\nEstos son los asientos libres:")
            print(asientos_libres)
            break
        else:
            print("\nEl nombre no coincide con la reserva del asiento. Por favor, intentelo de nuevo.\n")
   
    while True:
        asiento_elegido2 = int(input("\n¿A qué asiento desea cambiar su reserva? \n"))
        if asiento_elegido2 in asientos_libres:
            Asientos[asiento_elegido2]["Estado"] = "Ocupado"
            Asientos[asiento_elegido2]["Nombre"] = nombre
            asientos_libres.remove(asiento_elegido2)
            print("\nCambio realizado con éxito.\n")
            break
        elif 0 < asiento_elegido2 <= 10:
            print("\nEl asiento que ha elegido ya está ocupado. Por favor, elija otro.\n")
        else:
            print("\nEl asiento que ha elegido no existe. Por favor, elija un asiento válido.\n")
   
    return Asientos