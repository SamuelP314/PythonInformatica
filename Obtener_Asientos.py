def Obtener_Asientos(Asientos):

    asientos_libres=[]
    asientos_ocupados=[]

    for Asiento, Estado in Asientos.items():
       if Estado["Estado"] == "Libre":
           asientos_libres.append(int(Asiento))


    for Asiento, Estado in Asientos.items():
       if Estado["Estado"] == "Ocupado":
           asientos_ocupados.append(int(Asiento))
    
    try:
        opcion2 = int(input("\n\n1- Mostrar todos los asientos\n2- Mostrar asientos libres\n3- Mostrar asientos ocupados\n\n"))
        if opcion2 == 1:
            print(Asientos)
        elif opcion2 == 2:
            print(asientos_libres)
        elif opcion2 == 3:
            print(asientos_ocupados)
        else:
            print("\nOpción no válida. Por favor, elija una opción definida.\n")
    except ValueError:
        print("\nOpción no válida. Por favor, elija una opción definida.\n")