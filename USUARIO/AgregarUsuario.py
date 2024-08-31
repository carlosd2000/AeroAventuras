#lista de usuarios
usuariosAdd = []

#funcion agregar
def AgregarU (usuariosAdd):
    
    #cantidad de veces a agregar persona
    
    N=1
    
    if N == 1:
        nombre=str(input("ingrse nombre"))
        cedula= int(input("ingrse cedula"))
        contraseña= int(input("ingrse contraseña"))
        usuario= {"nombre" :nombre,"cedula" : cedula, "contraseña": contraseña}
        
        usuariosAdd.append(usuario)
    else:
        
        print ("usuario agregado")
    