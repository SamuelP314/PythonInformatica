def Cancelar_Reserva(Asientos):
   
    asientos_libres = [int(Asiento) for Asiento, Estado in Asientos.items() if Estado["Estado"] == "Libre"]
   
    while True:
        asiento_elegido = int(input("\n¿Cuál es el número del asiento del cual quiere cancelar la reserva? \n"))
        if asiento_elegido not in asientos_libres and 0 < asiento_elegido <= 10:
            break
        elif asiento_elegido in asientos_libres:
            print("\nSe ha debido de confundir, el asiento introducido está libre. Por favor, intentelo de nuevo.\n")
        else:
            print("\nSe ha debido de confundir, el asiento no existe. Por favor, intentelo de nuevo.\n")
   
    while True:
        nombre = input("\nPor motivos de seguridad, necesitamos el nombre al que se puso la reserva. \n")
        if Asientos[asiento_elegido]["Nombre"] == nombre:
            Asientos[asiento_elegido]["Estado"] = "Libre"
            Asientos[asiento_elegido]["Nombre"] = ""
            asientos_libres.append(asiento_elegido)
            asientos_libres.sort()
            print("\nReserva cancelada con éxito.\n")
            break
        else:
            print("\nEl nombre no coincide con la reserva del asiento. Por favor, intentelo de nuevo.\n")
   
    return Asientos, asientos_libres