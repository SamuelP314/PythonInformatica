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
    try:
        opcion=int(input( "\n ¿Que desea hacer? \n \n 1- Reservar un nuevo asiento \n 2- Cancelar una reserva \n 3- Cambiar un asiento \n 0- Salir\n \n"))
    except:
        opcion=_
    match opcion:
        case 1:
            Asientos = Reservar_Asiento(Asientos)
        case 2:
            Asientos = Cancelar_Reserva(Asientos)
        case 3:
            Asientos = Cambiar_Asiento(Asientos)
        case 0:
            break
        case _:
            print("\nError. Por favor, elija una opción definida.\n")



print(Asientos)