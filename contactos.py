#Opcion 1 agregar areas
#Estructura de como es Ejemplo de una posible lista areas: [ (506, “Costa Rica”), (47, “Noruega”), (502, “Guatemala”) ]

def agregar_areas(areas):
    while True:
        print("             LISTA DIGITAL DE CONTACTOS")
        print()
        print("             REGISTRAR ÁREAS: AGREGAR")
        print()
        area = input("Área (C para cancelar):                    ")#En esta pantalla primero pide (input) al usuario el dato “Área” que va a agregar.Y si pone c se sale
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




#Opcion 2 Consultar areas
                
def consultar_areas(areas):
    while True:
        print("             LISTA DIGITAL DE CONTACTOS")
        print()
        print("             REGISTRAR ÁREAS: CONSULTAR")
        area = input("Área (C para cancelar): ")
        if area == "C" or area == "c":#Si el user pone c entonces sale
            break
        if not area.isdigit():#Validar que sea numero
            print("El área debe ser un número")
            continue
        area = int(area)#Convertir el área de texto a entero
        encontrado = False#Suponer que todavía no se encontró el área
        for dato in areas:#Voy por los datos en las listas
            if dato[0] == area:#Si esta
                print("Área:", dato[0])#Despliego el mensaje y lo que hay que dar
                print("Nombre del área:", dato[1])
                while True:
                    opcion = input("OPCIÓN A-ACEPTAR _")#Al final de la operación esta se debe ACEPTAR para desplegar nuevamente esta ventana y permitir más operaciones de consulta.
                    if opcion == "A" or opcion == "a":
                        break
                    else:
                        print("Ingrese A para aceptar")
            encontrado = True#Se encontró el área
            break
        if encontrado == False:#El programa valida que este código exista en la lista
            print("ESTA ÁREA NO ESTÁ REGISTRADA, NO SE PUEDE CONSULTAR")



#Opcion 3 modificar areas

def modificar_areas(areas):
    while True:#Repetir para permitir mas modificaciones
        print("LISTA DIGITAL DE CONTACTOS")
        print()
        print("REGISTRAR ÁREAS: MODIFICAR")
        print()
        area = input("Área (C para cancelar): ")#Pedir el codigo del area a modificar
        if area == "C" or area == "c":#Si el user pone c entonces sale
            break
        if not area.isdigit():#Validar que sea numero
            print("El área debe ser un número")
            continue
        area = int(area)#Convertir el área de texto a entero
        encontrado = False#Suponer que todavía no se encontró el área
        for i in range(len(areas)):#Recorrer las posiciones de la lista
            dato = areas[i]#Obtener los datos del area actual
            if dato[0] == area:#Comprobar si el codigo existe
                print("Área:", dato[0])#Despliego el mensaje y lo que hay que dar
                print("Nombre del área:", dato[1])
                encontrado = True#Indicar que encontramos el area
                while True:
                    modificar = input("MODIFICACIÓN: ")#Pedir el nuevo nombre

                    if modificar == "":#Si presiona Enter mantiene el nombre anterior
                        modificar = dato[1]

                    if len(modificar) > 40:#Validar que no supere los 40 caracteres
                        print("El nombre del área no puede superar los 40 caracteres")
                        continue
                    break#Salir del ciclo cuando el nombre es valido
                while True:
                    opcion = input("OPCIÓN A-ACEPTAR C-CANCELAR: ")#Pedir confirmacion para guardar o cancelar
                    if opcion == "A" or opcion == "a":
                        areas[i] = (area, modificar)#Reemplazar la tupla con el nuevo nombre
                        break
                    elif opcion == "C" or opcion == "c":
                        break#Cancelar sin guardar cambios
                    else:
                        print("Ingrese A o C")
                    break#Salir del for porque ya encontramos el area
        if encontrado == False:#Si no existe el area mostrar un mensaje
            print("ESTA ÁREA NO ESTÁ REGISTRADA, NO SE PUEDE MODIFICAR")
                        
                

#Opcion 4 eliminar areas

def eliminar_areas(areas):
    while True:#Repetir hasta que el usuario cancele
        print("LISTA DIGITAL DE CONTACTOS")
        print()
        print("REGISTRAR ÁREAS: ELIMINAR")
        print()
        area = input("Área (C para cancelar): ")#Pedir el area que quiere eliminar
        if area == "C" or area == "c":#Si pone C regresa al menu anterior
            break

        if not area.isdigit():#Validar que sea un numero
            print("El área debe ser un número")
            continue

        area = int(area)#Convertir el area de texto a entero
        encontrado = False#Suponer que todavia no se encontro el area
        for i in range(len(areas)):#Recorrer la lista de areas
            dato = areas[i]#Obtener los datos de cada area
            if dato[0] == area:#Comprobar si el codigo coincide
                print("Área:", dato[0])
                print("Nombre del área:", dato[1])
                encontrado = True#El area si existe
                while True:#Repetir hasta que ponga A o C
                    opcion = input("OPCIÓN A-ACEPTAR C-CANCELAR: ")
                    if opcion == "A" or opcion == "a":
                        areas.pop(i)#Eliminar el area si acepta
                        break
                    elif opcion == "C" or opcion == "c":
                        break#Cancelar sin eliminar el area
                    else:
                        print("Ingrese A o C")#Si pone otra cosa vuelve a preguntar
                break#Terminar la busqueda despues de aceptar o cancelar
        if encontrado == False:
            print("ESTA ÁREA NO ESTÁ REGISTRADA, NO SE PUEDE ELIMINAR")#Si el area no existe
                 

        
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
                consultar_areas(areas)
            case "3":
                modificar_areas(areas)
            case "4":
                eliminar_areas(areas)
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
