
#print ("estos son los usuarios en la lista", usuarios)

lista= []

def EliminarU (lista):
    eliminar= int(input("ingrese cedula para eliminar"))
    
    lista= [usuario for usuario in lista if usuario['cedula'] != eliminar]
    
    ##print ("lista actualizada", lista)
    
    return lista