Asientos = {
    "Conductor": {"Estado": "Ocupado", "Nombre": "Santi"},
    1: {"Estado": "Libre", "Nombre": ""},
    2: {"Estado": "Libre", "Nombre": ""},
    3: {"Estado": "Libre", "Nombre": ""},
    4: {"Estado": "Libre", "Nombre": ""},
    5: {"Estado": "Libre", "Nombre": ""},
    6: {"Estado": "Libre", "Nombre": ""},
    7: {"Estado": "Libre", "Nombre": ""},
    8: {"Estado": "Libre", "Nombre": ""},
    9: {"Estado": "Ocupado", "Nombre": "Samuel"},
    10: {"Estado": "Ocupado", "Nombre": "Acher"}
}






def Reservar_Asiento():


    asientos_libres = []


    print("\nEstos son los asientos libres:")


    for Asiento, Estado in Asientos.items():
       if Estado["Estado"] == "Libre":
           asientos_libres.append(int(Asiento))


    print(asientos_libres)


    while True:


        asiento_elegido = int(input("\n¿Cual asiento desea reservar? \n "))


        if asiento_elegido in asientos_libres:
            nombre = input("\n¿Cual es su nombre? \n")
            Asientos[asiento_elegido]["Estado"] = "Ocupado"
            Asientos[asiento_elegido]["Nombre"] = nombre
            asientos_libres.remove(asiento_elegido)
            break


        elif 0 < asiento_elegido <= 10:
            print("\nEl asiento que ha elegido ya esta ocupado.\n ")


        else:
            print("\nEl asiento que ha elegido no existe.\n ")


    return Asientos, asientos_libres






def Cancelar_Reserva():
   
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






def Cambiar_Asiento():
    asientos_libres = [int(Asiento) for Asiento, Estado in Asientos.items() if Estado["Estado"] == "Libre"]
   
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
   
    return Asientos, asientos_libres






while True:
    opcion=int(input( "\n ¿Que desea hacer? \n \n 1- Reservar un nuevo asiento \n 2- Cancelar una reserva \n 3- Cambiar un asiento \n 0- Salir\n \n"))
    if opcion==1:
        Reservar_Asiento()
    elif opcion==2:
        Cancelar_Reserva()
    elif opcion==3:
        Cambiar_Asiento()
    elif opcion==0:
        break
    else:
        print("\nError. Por favor, elija una opción definida.\n")




print(Asientos)