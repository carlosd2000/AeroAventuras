usuariosAdd = []

# Función para editar usuarios
def EditarU(usuariosAdd):
    print ("esta es la lista actual", usuariosAdd)
    cedula = int(input("Ingrese la cédula del usuario a editar: "))
    for i in usuariosAdd:
        if i["cedula"] == cedula:
            nueva_cedula = int(input("ingrese nueva cc: "))
            nuevo_nombre = input("Ingrese nuevo nombre: ")
            nueva_contraseña = int(input("Ingrese nueva contraseña: "))
            
            if nueva_cedula:
                i["cedula"] = nueva_cedula
            if nuevo_nombre:
                i["nombre"] = nuevo_nombre
                
            if nueva_contraseña:
                i["contraseña"] = nueva_contraseña
            
            print("lista actualizada:", usuariosAdd)
            break
        
        return usuariosAdd
    else:
        print("Usuario no encontrado.")
    