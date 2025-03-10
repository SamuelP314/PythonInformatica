from Reservar_Asiento import *
from Cancelar_Reserva import *
from Cambiar_Asiento import *



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



while True:
    opcion=int(input( "\n ¿Que desea hacer? \n \n 1- Reservar un nuevo asiento \n 2- Cancelar una reserva \n 3- Cambiar un asiento \n 0- Salir\n \n"))
    if opcion==1:
        Reservar_Asiento(Asientos)
    elif opcion==2:
        Cancelar_Reserva(Asientos)
    elif opcion==3:
        Cambiar_Asiento(Asientos)
    elif opcion==0:
        break
    else:
        print("\nError. Por favor, elija una opción definida.\n")



print(Asientos)