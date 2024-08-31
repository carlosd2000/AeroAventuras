usuariosAdd = []

# Función para editar usuarios
def EditarU(usuariosAdd):
    cedula = int(input("Ingrese la cédula del usuario a editar: "))
    for usuario in usuariosAdd:
        if usuario["cedula"] == cedula:
            nueva_cedula = int(input("ingrese nueva cc: "))
            nuevo_nombre = input("Ingrese nuevo nombre (deje en blanco para no cambiar): ")
            nueva_contraseña = int(input("Ingrese nueva contraseña (deje en blanco para no cambiar): "))
            
            if nueva_cedula:
                usuario["cedula"] = nueva_cedula
            if nuevo_nombre:
                usuario["nombre"] = nuevo_nombre
                
            if nueva_contraseña:
                usuario["contraseña"] = nueva_contraseña
            
            print("Usuario actualizado:", usuariosAdd)
            break
    else:
        print("Usuario no encontrado.")
    