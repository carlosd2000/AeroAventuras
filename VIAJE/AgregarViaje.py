
viajesAdd = []

hoteles = {"1": "hotel 5 estrellas", "2": "hotel 3 estrellas", "3": "hotel 1 estrella"}

def AgregarViaje(viajesAdd):
    N = 1  # cantidad de veces a agregar persona
    
    if N == 1:
        destino = input("Ingrese cuidad de destino: ")
        id = int (input ("ingrese un nuemero de id para su paquete:"))
        hotel = mostrarOpciones(list(hoteles.keys()), "escoja hotel")
        
        if hotel == "1":
            Valor_hotel = 1000000
        elif hotel == "2":
            Valor_hotel = 500000
        elif hotel == "3":
            Valor_hotel = 250000
        else:
            print("Opción de hotel no válida")
            return 
        
        dias = int(input("Ingrese días a quedarse: "))
        valor_dia = dias * 100000
        total = Valor_hotel + valor_dia
        
        viaje = {"id": id, "destino": destino, "hotel": hoteles[hotel], "dias": dias, "total": total}
        viajesAdd.append(viaje)
        
        return viajesAdd
    else:
        print("Error, vuelva a intentarlo")

def mostrarOpciones(lista, tipo):
    print(f"Seleccione su {tipo}: ")
    for indice, valor in enumerate(lista, 1):
        print(f"{indice}. {hoteles[valor]}")
    opcion = int(input(f"Seleccione una opción (1-{len(lista)}): "))
    return lista[opcion - 1]

""""
def crearDestino(id_paquete):
    destino = mostrarOpciones(list(destinos_hoteles.keys()), "destino")
    hotel = mostrarOpciones(destinos_hoteles[destino], "hotel")
    dia = int(input("Cuantos dias se va hospedar: "))
    aerolineas = mostrarOpciones(aerolinea, "aerolínea")
    precio = random.randint(200, 1000)
    
"""