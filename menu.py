from USUARIO.AgregarUsuario import AgregarU
from USUARIO.EditarUsuario import EditarU
from USUARIO.EliminarUsuario import EliminarU
usuarios = []

print ("==========menu==========")

print("escriba el numero de la opcion que desea")
print("1) Agregar usuario")
print("2) Eliminar usuario")
print("3) Editar usuario")
print("4) Agregar destino")
print("5) Cambiar destino")
print("6) Eliminar destino")
print("7) Salir")
print("========================")

while True:
    
    opcion = input("Selecciona una opcion: ")
        
    if opcion == "1":
        AgregarU(usuarios)
        print("lista de usuarios", usuarios) 
        print("========================")          
    elif opcion == "2":
        usuarios= EliminarU(usuarios)
        print("lista de usuarios actualizada", usuarios) 
        print("========================")    
    elif opcion == "3":
        usuarios=EditarU(usuarios)
        print("========================")
        
    elif opcion == "7":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, intenta de nuevo.")
            
