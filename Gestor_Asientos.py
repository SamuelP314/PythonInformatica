from Reservar_Asiento import *
from Cancelar_Reserva import *
from Cambiar_Asiento import *
from Obtener_Asientos import *

Asientos = {
    "Conductor": {"Estado": "Asignado", "Nombre": "Santi"},
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
        opcion = int(input("\n¿Qué desea hacer?\n\n1- Reservar un nuevo asiento\n2- Cancelar una reserva\n3- Cambiar un asiento\n4- Mostrar lista de asientos \n0- Salir\n\n"))
        
        if opcion == 1:
            Reservar_Asiento(Asientos)
        elif opcion == 2:
            Cancelar_Reserva(Asientos)
        elif opcion == 3:
            Cambiar_Asiento(Asientos)
        elif opcion == 4:
            Obtener_Asientos(Asientos)
        elif opcion == 0:
            print("Saliendo del sistema...")
            break
        else:
            print("\nOpción no válida. Por favor, elija una opción definida.\n")
    
    except ValueError:
        print("\nOpción no válida. Por favor, elija una opción definida.\n")