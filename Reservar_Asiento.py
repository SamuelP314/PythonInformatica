def Reservar_Asiento(Asientos):
<<<<<<< HEAD
    
    asientos_libres = []
=======

    asientos_libres = []

>>>>>>> 7fe9030b52ba26b5817f4b9ccc2c4313b78359a8
    print("\nEstos son los asientos libres:")

    for Asiento, Estado in Asientos.items():
       if Estado["Estado"] == "Libre":
           asientos_libres.append(int(Asiento))

    print(asientos_libres)

    while True:
        asiento_elegido = int(input("\n¿Cual asiento desea reservar? \n "))
<<<<<<< HEAD

=======
>>>>>>> 7fe9030b52ba26b5817f4b9ccc2c4313b78359a8
        if asiento_elegido in asientos_libres:
            nombre = input("\n¿Cual es su nombre? \n")
            Asientos[asiento_elegido]["Estado"] = "Ocupado"
            Asientos[asiento_elegido]["Nombre"] = nombre
            asientos_libres.remove(asiento_elegido)
            break
        elif 0 < asiento_elegido <= 10:
            print("\nEl asiento que ha elegido ya esta ocupado.\n ")
<<<<<<< HEAD

        else:
            print("\nEl asiento que ha elegido no existe.\n ")
   
    return Asientos
=======
        else:
            print("\nEl asiento que ha elegido no existe.\n ")

    return Asientos, asientos_libres
>>>>>>> 7fe9030b52ba26b5817f4b9ccc2c4313b78359a8
