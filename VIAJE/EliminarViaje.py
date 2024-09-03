viajesDelete = []

def EliminarViaje(viajesDelete):
    if not viajesDelete:
        print("No hay viajes para eliminar.")
        return viajesDelete
    
    id_paquete = int(input("Ingrese el ID del paquete que desea eliminar: "))
    
    for viaje in viajesDelete:
        if viaje["id"] == id_paquete:
            viajesDelete.remove(viaje)
            print(f"El viaje con ID {id_paquete} ha sido eliminado.")
            return viajesDelete
        else:
            print(f"No se encontró ningún viaje con el ID {id_paquete}.")
            return viajesDelete