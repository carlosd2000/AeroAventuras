viajesEditar = []
hoteles = {"1": "hotel 5 estrellas", "2": "hotel 3 estrellas", "3": "hotel 1 estrella"}

def EditarViaje(viajesEditar):
    print("Esta es la lista actual de viajes:", viajesEditar)
    id_paquete = int(input("Ingrese el ID del paquete a editar: "))
    
    for viaje in viajesEditar:
        if viaje["id"] == id_paquete:
            nuevo_id = int(input("Ingrese nuevo ID : "))
            nuevo_destino = input("Ingrese nuevo destino: ")
            nuevo_hotel = mostrarOpciones(list(hoteles.keys()), "escoja nuevo hotel")
            nuevos_dias = int(input("Ingrese nuevos días a quedarse: "))
            
            if nuevo_hotel == "1":
                Valor_hotel = 1000000
            elif nuevo_hotel == "2":
                Valor_hotel = 500000
            elif nuevo_hotel == "3":
                Valor_hotel = 250000
            else:
                
                print("Opción de hotel no válida")
                return viajesEditar
            
            valor_dia = nuevos_dias * 100000
            total = Valor_hotel + valor_dia
            
            if nuevo_id:
                viaje["id"] = nuevo_id
            if nuevo_destino:
                viaje["destino"] = nuevo_destino
            if nuevo_hotel:
                viaje["hotel"] = hoteles[nuevo_hotel]
            if nuevos_dias:
                viaje["dias"] = nuevos_dias
                viaje["total"] = total
            
            ##print("Lista actualizada de viajes:", viajesEditar)
            break
    else:
        print("Paquete no encontrado.")
    
    return viajesEditar

def mostrarOpciones(lista, tipo):
    print(f"Seleccione su {tipo}: ")
    for indice, valor in enumerate(lista, 1):
        print(f"{indice}. {hoteles[valor]}")
    opcion = int(input(f"Seleccione una opción (1-{len(lista)}): "))
    return lista[opcion - 1]

