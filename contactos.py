#Opcion 1 agregar areas
#Estructura de como es Ejemplo de una posible lista areas: [ (506, “Costa Rica”), (47, “Noruega”), (502, “Guatemala”) ]
def agregar_areas(areas):
    while True:
        print("             LISTA DIGITAL DE CONTACTOS")
        print()
        print("             REGISTRAR ÁREAS: AGREGAR")
        print()
        area = input("Área                    ")#En esta pantalla primero pide (input) al usuario el dato “Área” que va a agregar.
        if area == "C" or area == "c":
            break
        if not area.isdigit():#La información de las áreas está en la lista areas, donde cada elemento es una tupla que tiene: - Área (entero >= 1 y <= 999) - Nombre del área (string entre 1 y 40 caracteres).
            print("El area debe ser un numero")
            continue
        area = int(area)#Convierto el dato ingresado a que sea enteros
        if area < 1 or area > 999:#Validando
            print("El área debe estar entre 1 y 999")
            continue
        repetido = False#Suponer que no hay repetidos
        for dato in areas:#Reviso los datos
            if dato[0] == area:#Si hay repetidos
                repetido = True#Hay repetidos
                break
        if repetido == True:#cuando hay repetidos
            print("ESTA ÁREA YA ESTÁ REGISTRADA, NO SE PUEDE AGREGAR")
            continue
        if repetido == False:#Si no hay repetidos
            nombre_area = input("Nombre del área         ")#Ingresar nombre de areas
            if len(nombre_area) < 1 or len(nombre_area) > 40:#Validar la cantidad de caracteres
                print("Nombre del area debe ser dentro de 1 a 40 caracteres")
                continue
            while True:#Repetir la pregunta de A o C cuando poner cosas nada que ver
                opcion = input("OPCIÓN A-ACEPTAR C-CANCELAR: ")
                if opcion == "A" or opcion == "a":
                    areas.append((area,nombre_area))#Si escoge A,lo agrego
                    break
                elif opcion == "C" or opcion =="c":
                    break#Si cancela pues termina
                else:
                    print("Ingrese A o C")
                    continue#Si pone algo que nada que ver

            

        
        
#1 Registrar areas
#La información de las áreas está en la lista areas, donde cada elemento es una tupla que tiene: - Área (entero >= 1 y <= 999) - Nombre del área (string entre 1 y 40 caracteres)

def registrar_areas(areas):
    while True:
        print("             LISTA DIGITAL DE CONTACTOS")
        print()
        print("                 REGISTRAR ÁREAS")
        print("1.     Agregar áreas")
        print("2.     Consultar áreas")
        print("3.     Modificar áreas")
        print("4.     Eliminar áreas")
        print("0.     Fin")
        opcion = input("       OPCIÓN _")
        match opcion:
            case "1":
                agregar_areas(areas)
            case "2":
                print("Llamar a la función para: 2. Consultar áreas")
            case "0":
                break
            case _:
                print("ESTA OPCIÓN NO EXISTE")
    return

#Funcion principal
#Lista digital de contactos
def principal():
    areas = [] 
    TIPOS_TELEFONO = ("M", "Móvil", "C", "Casa", "T", "Trabajo", "O", "Otro")
    while True:
        print("     LISTA DIGITAL DE CONTACTOS")#Haciendo lo mas parecido a lo que esta en el pdf posible
        print()
        print("1. Registrar áreas")
        print("2. Configuración de lista de contactos")
        print("3. Registrar contactos")
        print("4. Administrar grupos de contactos")
        print("5. Lista de contactos")
        print("6. Ayuda")
        print("7. Acerca de")
        print("0. Fin")
        print()
        opcion = input("   OPCIÓN _")
        match opcion:
            case "1":
                registrar_areas(areas) 
            case "2":
                print("Llamar a la función para: 2. Configuración de lista de contactos")
            case "0":
                break
            case _:
                print("ESTA OPCIÓN NO EXISTE")
    print("FIN DEL PROGRAMA")
                             
principal()
