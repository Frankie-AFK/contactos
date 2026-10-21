from datetime import datetime#Importar datetime para validar fechas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A3, landscape
TIPOS_TELEFONO = ("M", "Móvil", "C", "Casa", "T", "Trabajo", "O", "Otro")
from xml.sax.saxutils import escape



#Opcion 1.1 agregar areas
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
            while True:
                nombre_area = input("Nombre del área         ")#Ingresar nombre de areas
                if nombre_area.strip() == "" or len(nombre_area) > 40:#Validar la cantidad de caracteres
                    print("Nombre del area debe ser dentro de 1 a 40 caracteres")
                    continue
                break
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



#Opcion 1.2 Consultar areas
                
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



#Opcion 1.3 modificar areas

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
                    if modificar != "" and modificar.strip() == "":
                        print("El nombre del área no puede contener solo espacios")
                        continue
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
                        
                

#Opcion 1.4 eliminar areas

def eliminar_areas(areas,contactos,configuracion):
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
                        if len(configuracion) > 0:
                            if configuracion[0][0] == area:
                                print("ESTA ÁREA ESTÁ CONFIGURADA POR OMISIÓN, NO SE PUEDE ELIMINAR")
                                break
                        tiene_contactos = False
                        for contacto in contactos:
                            if contacto[1] == area:
                                tiene_contactos = True
                                break
                        if tiene_contactos == True:
                            print("EN ESTA ÁREA HAY CONTACTOS REGISTRADOS, NO SE PUEDE ELIMINAR")
                            break
                        else:
                            while True:
                                confirmar = input("CONFIRMA LA ELIMINACIÓN (SI/NO): ")
                                if confirmar == "SI" or confirmar == "si":
                                    areas.pop(i)
                                    print("Área eliminada correctamente")
                                    break
                                elif confirmar == "NO" or confirmar == "no":
                                    print("Eliminación cancelada")
                                    break
                                else:
                                    print("Ingrese SI o NO")
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

def registrar_areas(areas,contactos,configuracion):
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
                eliminar_areas(areas,contactos,configuracion)
            case "0":
                break
            case _:
                print("ESTA OPCIÓN NO EXISTE")
    return



#2 Configuracion de la lista de contactos

def configurar_lista_contactos(areas,configuracion):
    while True:
        print("       LISTA DIGITAL DE CONTACTOS")
        print()
        print("CONFIGURACIÓN DE LA LISTA DE CONTACTOS")
        print()
        area = input("Área por omisión       ")#Pedir el area que se va a usar por omision
        if not area.isdigit():#Validar que sea un numero
            print("El área debe ser un número")
            continue#Volver a pedir el area
        area = int(area)#Convertir el area de texto a entero
        encontrado = False#Suponer que el area todavia no esta registrada
        for dato in areas:#Recorrer las areas registradas
            if dato[0] == area:#Comparar el codigo del area
                print("Nombre del area:",dato[1])
                encontrado = True#El area si existe
                break#Dejar de buscar
        if encontrado == False:#Si no encontro el area
            print("ESTA ÁREA NO ESTÁ REGISTRADA, NO SE PUEDE SELECCIONAR")
            continue#Volver a pedir el area
        while True:#Pedir el tipo de telefono hasta que sea valido
            tipo = input("Tipo de teléfono por omisión (M/C/T/O): ")
            if tipo == "M" or tipo == "m":#M o m significa movil
                print("Móvil")
                break
            elif tipo == "C" or tipo == "c":#C o c significa casa
                print("Casa")
                break
            elif tipo == "T" or tipo == "t":#T o t significa trabajo
                print("Trabajo")
                break
            elif tipo == "O" or tipo == "o":#O o o significa otro
                print("Otro")
                break
            else:
                print("ESTE TIPO DE TELÉFONO NO EXISTE, NO SE PUEDE SELECCIONAR")
        if tipo == "m":#Convertir las letras minusculas a mayusculas
            tipo = "M"
        elif tipo == "c":
            tipo = "C"
        elif tipo == "t":
            tipo = "T"
        elif tipo == "o":
            tipo = "O"
        while True:#Pedir confirmacion antes de guardar
            opcion = input("OPCIÓN A-ACEPTAR C-CANCELAR: ")
            if opcion == "A" or opcion == "a":#Si acepta guardar la configuracion
                configuracion.clear()#Quitar la configuracion anterior
                configuracion.append((area, tipo))#Guardar el area y el tipo de telefono
                print("Configuración aceptada")
                return#Regresar al menu principal
            elif opcion == "C" or opcion == "c":#Si cancela no guardar los cambios
                print("Configuración cancelada")
                return#Regresar al menu principal
            else:
                print("Ingrese A o C")#Si pone otra cosa pedir de nuevo
            


#Opcion 3.1 Agregar Contactos

def agregar_contactos(contactos, areas, configuracion):
    while True:
        print("LISTA DIGITAL DE CONTACTOS")
        print()
        print("REGISTRAR CONTACTOS: AGREGAR")
        print()
        telefono = input("Teléfono (C para cancelar): ")
        if telefono == "C" or telefono == "c":
            break
        if not telefono.isdigit():
            print("El teléfono debe contener solo números")
            continue
        if len(telefono) < 5 or len(telefono) > 12:
            print("El teléfono debe tener entre 5 y 12 dígitos")
            continue
        telefono = int(telefono)#Convertir el telefono a entero
        area = input("Área (Enter para usar área por omisión): ")
        if area == "":
            if len(configuracion) == 0:
                print("Primero debe configurar el área por omisión")
                continue
            area = configuracion[0][0]
        if not str(area).isdigit():#Verificar que el area sea un numero
            print("El área debe ser un número")
            continue
        area = int(area)#Convertir el area a entero
        encontrado = False#Suponer que el area no existe
        for dato in areas:#Recorrer las areas registradas
            if dato[0] == area:#Comparar los codigos
                encontrado = True#El area existe
                print("Nombre del área:", dato[1])
                break
        if encontrado == False:#Si el area no esta registrada
            print("ESTA ÁREA NO ESTÁ REGISTRADA, NO SE PUEDE SELECCIONAR")
            continue
        repetido = False
        for dato in contactos:
            if dato[0] == telefono and dato[1] == area:
                repetido = True
                break
        if repetido == True:
            print("ESTE TELÉFONO YA ESTÁ REGISTRADO EN ESTA ÁREA")
            continue
        tipo = input("Tipo de teléfono (M/C/T/O, Enter por omisión): ")
        if tipo == "":
            if len(configuracion) == 0:
                print("Primero debe configurar el tipo de teléfono por omisión")
                continue
            tipo = configuracion[0][1]
        if tipo == "m":
            tipo = "M"
        elif tipo == "c":
            tipo = "C"
        elif tipo == "t":
            tipo = "T"
        elif tipo == "o":
            tipo = "O"
        if tipo != "M" and tipo != "C" and tipo != "T" and tipo != "O":
             print("ESTE TIPO DE TELÉFONO NO EXISTE, NO SE PUEDE SELECCIONAR")
             continue
        while True:
            nombre = input("Nombre del contacto: ")
            if nombre.strip() == "" or len(nombre) > 50:
                print("El nombre debe tener entre 1 y 50 caracteres")
                continue
            break
        while True:
            correo = input("Correo electrónico: ")
            if correo.count("@") != 1:
                print("El correo debe tener el formato parte1@parte2")
                continue
            partes = correo.split("@")
            if partes[0] == "" or partes[1] == "":
                print("El correo debe tener texto antes y despues del @")
                continue
            if " " in correo:
                print("El correo no puede contener espacios")
                continue
            break
        while True:
            direccion = input("Dirección física: ")
            if len(direccion) > 80:
                print("La dirección no puede superar los 80 caracteres")
                continue
            break
        while True:
            fecha = input("Fecha de nacimiento (dd/mm/aaaa, Enter si no se conoce): ")
            if fecha == "":
                fecha = 0
                break
            try:
                partes_fecha = fecha.split("/")
                if len(partes_fecha) != 3:
                    print("El formato de la fecha no es válido")
                    continue
                if len(partes_fecha[0]) != 2 or len(partes_fecha[1]) != 2 or len(partes_fecha[2]) != 4:
                    print("La fecha debe tener el formato dd/mm/aaaa")
                    continue
                if not partes_fecha[0].isdigit() or not partes_fecha[1].isdigit() or not partes_fecha[2].isdigit():
                    print("La fecha debe contener solo números")
                    continue
                if partes_fecha[2] == "0000":
                    fecha_validar = partes_fecha[0] + "/" + partes_fecha[1] + "/2000"
                else:
                    fecha_validar = fecha
                datetime.strptime(fecha_validar, "%d/%m/%Y")
                break
            except ValueError:
                print("La fecha de nacimiento no es válida")
        while True:
            pasatiempos = input("Pasatiempos: ")
            if len(pasatiempos) > 60:
                print("Los pasatiempos no pueden superar los 60 caracteres")
                continue
            break
        while True:
            notas = input("Notas: ")
            if len(notas) > 60:
                print("Las notas no pueden superar los 60 caracteres")
                continue
            break
        while True:#Pedir confirmacion hasta que sea valida
            opcion = input("OPCIÓN A-ACEPTAR C-CANCELAR: ")
            if opcion == "A" or opcion == "a":
                contactos.append([telefono, area, tipo, nombre, correo, direccion, fecha, pasatiempos, notas])
                print("Contacto registrado correctamente")
                break
            elif opcion == "C" or opcion == "c":
                print("Registro cancelado")
                break
            else:
                print("Ingrese A o C")
            
            

#Opcion 3.2 Consultar Contactos

def consultar_contactos(contactos):
    if len(contactos) == 0:
        print("NO HAY CONTACTOS REGISTRADOS")
        return
    while True:#Permitir consultar varios contactos
        print("LISTA DIGITAL DE CONTACTOS")
        print()
        print("REGISTRAR CONTACTOS: CONSULTAR")
        print()
        telefono = input("Teléfono (C para cancelar): ")#Pedir el numero de telefono
        if telefono == "C" or telefono == "c":#Regresar al menu anterior
            return
        area = input("Área: ")#Pedir el codigo de area
        if not telefono.isdigit() or not area.isdigit():#Verificar que sean numeros
            print("EL TELÉFONO Y EL ÁREA DEBEN SER NUMÉRICOS")
            continue
        if len(telefono) < 5 or len(telefono) > 12:#Validar cantidad de digitos
            print("EL TELÉFONO DEBE TENER ENTRE 5 Y 12 DÍGITOS")
            continue
        telefono = int(telefono)
        area = int(area)
        encontrado = False#Indicar si encontramos el contacto
        for contacto in contactos:#Recorrer la lista de contactos
            if contacto[0] == telefono and contacto[1] == area:
                encontrado = True
                break
        if encontrado == False:
            print("ESTE CONTACTO NO ESTA REGISTRADO, NO SE PUEDE CONSULTAR")
            continue
        print("DATOS DEL CONTACTO")
        print("Teléfono:", contacto[0])
        print("Área:", contacto[1])
        print("Tipo de teléfono:", contacto[2])
        print("Nombre:", contacto[3])
        print("Correo electrónico:", contacto[4])
        print("Dirección física:", contacto[5])
        print("Fecha de nacimiento:", contacto[6])
        print("Pasatiempos:", contacto[7])
        print("Notas:", contacto[8])
        while True:#Esperar que el usuario acepte la consulta
            opcion = input("OPCIÓN A-ACEPTAR: ")
            if opcion == "A" or opcion == "a":
                break
            else:
                print("Ingrese A para aceptar")



#Opcion 3.3 Modificar Contactos

def modificar_contactos(contactos):
    if len(contactos) == 0:
        print("NO HAY CONTACTOS REGISTRADOS")
        return
    while True:#Permitir modificar varios contactos
        print("LISTA DIGITAL DE CONTACTOS")
        print()
        print("REGISTRAR CONTACTOS: MODIFICAR")
        print()
        telefono = input("Teléfono (C para cancelar): ")#Pedir el numero de telefono
        if telefono == "C" or telefono == "c":#Regresar al menu anterior
            return
        area = input("Área: ")#Pedir el codigo de area
        if not telefono.isdigit() or not area.isdigit():
            print("EL TELÉFONO Y EL ÁREA DEBEN SER NUMÉRICOS")
            continue
        if len(telefono) < 5 or len(telefono) > 12:
            print("EL TELÉFONO DEBE TENER ENTRE 5 Y 12 DÍGITOS")
            continue
        telefono = int(telefono)
        area = int(area)
        encontrado = False#Indicar si encontramos el contacto
        for contacto in contactos:#Recorrer la lista de contactos
            if contacto[0] == telefono and contacto[1] == area:
                encontrado = True
                break
        if encontrado == False:
            print("ESTE CONTACTO NO ESTÁ REGISTRADO, NO SE PUEDE MODIFICAR")
            continue
        print("Nombre del contacto:", contacto[3])
        while True:
            nuevo_nombre = input("MODIFICACIÓN: ")
            if (nuevo_nombre != "" and nuevo_nombre.strip() == "") or len(nuevo_nombre) > 50:
                print("EL NOMBRE NO PUEDE SUPERAR 50 CARACTERES")
                continue
            break
        print("Correo electrónico:", contacto[4])
        while True:
            nuevo_correo = input("MODIFICACIÓN: ")
            if nuevo_correo == "":
                break
            if nuevo_correo.count("@") != 1 or " " in nuevo_correo:
                print("CORREO ELECTRÓNICO INVÁLIDO")
                continue
            partes = nuevo_correo.split("@")
            if partes[0] == "" or partes[1] == "":
                print("CORREO ELECTRÓNICO INVÁLIDO")
                continue
            break
        print("Dirección física:", contacto[5])
        while True:
            nueva_direccion = input("MODIFICACIÓN: ")
            if len(nueva_direccion) > 80:
                print("LA DIRECCIÓN NO PUEDE SUPERAR 80 CARACTERES")
                continue
            break
        print("Fecha de nacimiento:", contacto[6])
        while True:
            nueva_fecha = input("MODIFICACIÓN (dd/mm/aaaa, Enter para mantener): ")
            if nueva_fecha == "":
                break
            try:
                partes_fecha = nueva_fecha.split("/")
                if len(partes_fecha) != 3:
                    print("FECHA DE NACIMIENTO INVÁLIDA")
                    continue
                if len(partes_fecha[0]) != 2 or len(partes_fecha[1]) != 2 or len(partes_fecha[2]) != 4:
                    print("LA FECHA DEBE TENER EL FORMATO dd/mm/aaaa")
                    continue
                if not partes_fecha[0].isdigit() or not partes_fecha[1].isdigit() or not partes_fecha[2].isdigit():
                    print("LA FECHA DEBE CONTENER SOLO NÚMEROS")
                    continue
                if partes_fecha[2] == "0000":
                    fecha_validar = partes_fecha[0] + "/" + partes_fecha[1] + "/2000"
                else:
                    fecha_validar = nueva_fecha
                datetime.strptime(fecha_validar, "%d/%m/%Y")
                break
            except ValueError:
                print("FECHA DE NACIMIENTO INVÁLIDA")
        print("Pasatiempos:", contacto[7])
        while True:
            nuevos_pasatiempos = input("MODIFICACIÓN: ")
            if len(nuevos_pasatiempos) > 60:
                print("LOS PASATIEMPOS NO PUEDEN SUPERAR 60 CARACTERES")
                continue
            break
        print("Notas:", contacto[8])
        while True:
            nuevas_notas = input("MODIFICACIÓN: ")
            if len(nuevas_notas) > 60:
                print("LAS NOTAS NO PUEDEN SUPERAR 60 CARACTERES")
                continue
            break
        while True:#Pedir confirmacion para modificar el contacto
            opcion = input("OPCIÓN A-ACEPTAR C-CANCELAR: ")
            if opcion == "A" or opcion == "a":
                break
            elif opcion == "C" or opcion == "c":
                print("Modificación cancelada")
                break
            else:
                print("Ingrese A o C")
        if opcion == "A" or opcion == "a":#Guardar los cambios aceptados
            if nuevo_nombre != "":
                contacto[3] = nuevo_nombre
            if nuevo_correo != "":
                contacto[4] = nuevo_correo
            if nueva_direccion != "":
                contacto[5] = nueva_direccion
            if nueva_fecha != "":
                contacto[6] = nueva_fecha
            if nuevos_pasatiempos != "":
                contacto[7] = nuevos_pasatiempos
            if nuevas_notas != "":
                contacto[8] = nuevas_notas
            print("Contacto modificado correctamente")



#Opcion 3.4 Eliminar Contactos

def eliminar_contactos(contactos,grupos,contactos_por_grupo):
    if len(contactos) == 0:
        print("NO HAY CONTACTOS REGISTRADOS")
        return
    while True:#Permitir eliminar varios contactos
        print("LISTA DIGITAL DE CONTACTOS")
        print()
        print("REGISTRAR CONTACTOS: ELIMINAR")
        print()
        telefono = input("Teléfono (C para cancelar): ")
        if telefono == "C" or telefono == "c":
            return
        area = input("Área: ")
        if not telefono.isdigit() or not area.isdigit():
            print("EL TELÉFONO Y EL ÁREA DEBEN SER NUMÉRICOS")
            continue
        if len(telefono) < 5 or len(telefono) > 12:
            print("EL TELÉFONO DEBE TENER ENTRE 5 Y 12 DÍGITOS")
            continue
        telefono = int(telefono)
        area = int(area)
        encontrado = False#Indicar si encontramos el contacto
        for contacto in contactos:#Recorrer la lista de contactos
            if contacto[0] == telefono and contacto[1] == area:
                encontrado = True
                break
        if encontrado == False:
            print("ESTE CONTACTO NO ESTÁ REGISTRADO, NO SE PUEDE ELIMINAR")
            continue
        print("DATOS DEL CONTACTO A ELIMINAR")
        print("Teléfono:", contacto[0])
        print("Área:", contacto[1])
        print("Tipo de teléfono:", contacto[2])
        print("Nombre:", contacto[3])
        print("Correo electrónico:", contacto[4])
        print("Dirección física:", contacto[5])
        print("Fecha de nacimiento:", contacto[6])
        print("Pasatiempos:", contacto[7])
        print("Notas:", contacto[8])
        while True:#Confirmar si desea eliminar el contacto
            opcion = input("OPCIÓN A-ACEPTAR C-CANCELAR: ")
            if opcion == "A" or opcion == "a":
                pertenece = False
                for lista_grupo in contactos_por_grupo:
                    if (telefono, area) in lista_grupo:
                        pertenece = True
                        break
                if pertenece == True:
                    print("ESTE CONTACTO PERTENECE A UN GRUPO, NO SE PUEDE ELIMINAR")
                else:
                    while True:
                        confirmar = input("CONFIRMA LA ELIMINACIÓN (SI/NO): ")
                        if confirmar == "SI" or confirmar == "si":
                            contactos.remove(contacto)
                            print("Contacto eliminado correctamente")
                            break
                        elif confirmar == "NO" or confirmar == "no":
                            print("Eliminación cancelada")
                            break
                        else:
                            print("Ingrese SI o NO")
                break
            elif opcion == "C" or opcion == "c":
                print("Eliminación cancelada")
                break
            else:
                print("Ingrese A o C")
                continue
                        

                
#3.Registrar contactos

def registrar_contactos(contactos, areas, configuracion, grupos, contactos_por_grupo):#Funcion para mostrar el menu de registrar contactos
    while True:#Repetir el menu hasta que el usuario elija 0
        print("LISTA DIGITAL DE CONTACTOS")
        print()
        print("REGISTRAR CONTACTOS")
        print()
        print("1. Agregar contactos")
        print("2. Consultar contactos")
        print("3. Modificar contactos")
        print("4. Eliminar contactos")
        print("0. Fin")
        opcion = input("OPCIÓN _")#Pedir al usuario que elija una opcion
        match opcion:#Revisar cual opcion eligio el usuario
            case "1":#Opcion para agregar contactos
                agregar_contactos(contactos, areas, configuracion)
            case "2":#Opcion para consultar contactos
                consultar_contactos(contactos)
            case "3":#Opcion para modificar contactos
                modificar_contactos(contactos)
            case "4":#Opcion para eliminar contactos
                eliminar_contactos(contactos, grupos, contactos_por_grupo)
            case "0":#Regresar al menu principal
                break
            case _:#Si el usuario escribe una opcion que no existe
                print("ESTA OPCIÓN NO EXISTE")

    

#Opcion 4.1 Agregar grupos
                
def agregar_grupos(grupos, contactos_por_grupo):
    while True:
        print("LISTA DIGITAL DE CONTACTOS")
        print("ADMINISTRAR GRUPOS DE CONTACTOS")
        print("Agregar grupos")
        nombre = input("Nombre del grupo (C para cancelar): ")
        if nombre == "C" or nombre == "c":
            return
        if nombre.strip() == "" or len(nombre) > 40:
            print("EL NOMBRE DEL GRUPO DEBE TENER ENTRE 1 Y 40 CARACTERES")
            continue#Volver a pedir el nombre del grupo
        if nombre in grupos:#Verificar si el grupo ya esta registrado
            print("ESTE GRUPO YA ESTÁ REGISTRADO, NO SE PUEDE AGREGAR")
            continue
        while True:#Pedir confirmacion hasta que sea valida
            opcion = input("OPCIÓN A-ACEPTAR C-CANCELAR: ")
            if opcion == "A" or opcion == "a":#Si acepta agregar el grupo
                grupos.append(nombre)#Guardar el nombre del grupo
                contactos_por_grupo.append([])#Crear una lista vacia para los contactos del grupo
                print("Grupo registrado correctamente")
                break
            elif opcion == "C" or opcion == "c":#Si cancela la operacion
                print("Registro cancelado")
                break
            else:#Si escribe una opcion incorrecta
                print("Ingrese A o C")
                


#Opcion 4.2 Agregar contactos a los grupos
                
def agregar_contactos_grupos(grupos, contactos_por_grupo, contactos):
    while True:
        print("LISTA DIGITAL DE CONTACTOS")
        print()
        print("ADMINISTRAR GRUPOS DE CONTACTOS")
        print("Agregar contactos a los grupos")
        print()
        nombre = input("Nombre del grupo (C para cancelar): ")
        if nombre == "C" or nombre == "c":
            return
        if nombre not in grupos:#Verificar si el grupo existe
            print("ESTE GRUPO NO EXISTE, NO PUEDE AGREGARLE CONTACTOS")
            continue
        indice = grupos.index(nombre)#Buscar la posicion del grupo
        telefono = input("Teléfono: ")
        area = input("Área: ")
        if not telefono.isdigit() or not area.isdigit():#Verificar que sean numeros
            print("EL TELÉFONO Y EL ÁREA DEBEN SER NUMÉRICOS")
            continue
        if len(telefono) < 5 or len(telefono) > 12:#Verificar la cantidad de digitos
            print("EL TELÉFONO DEBE TENER ENTRE 5 Y 12 DÍGITOS")
            continue
        telefono = int(telefono)#Convertir el telefono a entero
        area = int(area)#Convertir el area a entero
        encontrado = False#Indicar si encontramos el contacto
        for contacto in contactos:#Recorrer la lista de contactos
            if contacto[0] == telefono and contacto[1] == area:
                encontrado = True
                print("Nombre contacto:", contacto[3])
                break
        if encontrado == False:#Si el contacto no esta registrado
            print("ESTE CONTACTO NO EXISTE, NO PUEDE AGREGARLO AL GRUPO")
            continue
        if (telefono, area) in contactos_por_grupo[indice]:#Verificar si ya esta en el grupo
            print("ESTE CONTACTO YA ESTÁ AGREGADO AL GRUPO")
            continue
        while True:#Pedir confirmacion hasta que sea valida
            opcion = input("OPCIÓN A-ACEPTAR C-CANCELAR: ")
            if opcion == "A" or opcion == "a":#Si acepta agregar el contacto
                contactos_por_grupo[indice].append((telefono, area))
                print("Contacto agregado al grupo correctamente")
                break
            elif opcion == "C" or opcion == "c":#Si cancela la operacion
                print("Operacion cancelada")
                break
            else:#Si escribe una opcion incorrecta
                print("Ingrese A o C")



#Opcion 4.3 Modificar grupos

def modificar_grupos(grupos, contactos_por_grupo):
    while True:
        print("LISTA DIGITAL DE CONTACTOS")
        print()
        print("ADMINISTRAR GRUPOS DE CONTACTOS")
        print("Modificar grupos")
        print()
        nombre = input("Nombre del grupo (C para cancelar): ")
        if nombre == "C" or nombre == "c":
            return
        if nombre not in grupos:#Verificar si el grupo existe
            print("GRUPO NO ESTÁ REGISTRADO, NO SE PUEDE MODIFICAR")
            continue
        indice = grupos.index(nombre)#Buscar la posicion del grupo
        nuevo_nombre = input("MODIFICACIÓN (Enter para mantener): ")#Pedir el nuevo nombre
        if nuevo_nombre == "":#Si no escribe nada, mantener el nombre actual
            nuevo_nombre = nombre
        if nuevo_nombre.strip() == "" or len(nuevo_nombre) > 40:#Verificar el limite de caracteres
            print("EL NOMBRE DEL GRUPO NO PUEDE SUPERAR 40 CARACTERES")
            continue
        if nuevo_nombre in grupos and nuevo_nombre != nombre:#Verificar si el nuevo grupo ya existe
            print("GRUPO YA EXISTE, EN CASO DE ACEPTAR LA OPERACIÓN LOS CONTACTOS SE LE AGREGARÁN")
            while True:#Pedir confirmacion si el grupo ya existe
                opcion = input("OPCIÓN A-ACEPTAR C-CANCELAR: ")
                if opcion == "A" or opcion == "a":
                    break
                elif opcion == "C" or opcion == "c":
                    print("Modificación cancelada")
                    break
                else:
                    print("Ingrese A o C")
            if opcion == "C" or opcion == "c":#Si cancela, volver a pedir el grupo
                continue
        if nuevo_nombre not in grupos:#Si el nuevo nombre no existe, cambiar el nombre
            while True:#Pedir confirmacion hasta que sea valida
                opcion = input("OPCIÓN A-ACEPTAR C-CANCELAR: ")
                if opcion == "A" or opcion == "a":
                    grupos[indice] = nuevo_nombre#Guardar el nuevo nombre del grupo
                    print("Grupo modificado correctamente")
                    break
                elif opcion == "C" or opcion == "c":
                    print("Modificación cancelada")
                    break
                else:
                    print("Ingrese A o C")
            if opcion == "C" or opcion == "c":
                continue
        elif nuevo_nombre == nombre:
            print("El nombre del grupo se mantiene igual")
        elif nuevo_nombre != nombre:#Si el grupo ya existe, unir los contactos
            nuevo_indice = grupos.index(nuevo_nombre)#Buscar la posicion del grupo nuevo
            for contacto in contactos_por_grupo[indice]:#Recorrer los contactos del grupo anterior
                if contacto not in contactos_por_grupo[nuevo_indice]:#Evitar contactos repetidos
                    contactos_por_grupo[nuevo_indice].append(contacto)#Agregar el contacto al nuevo grupo
            grupos.pop(indice)#Eliminar el grupo anterior
            contactos_por_grupo.pop(indice)#Eliminar su lista de contactos
            print("Grupo modificado correctamente")



#Opcion 4.4 Eliminar grupos

def eliminar_grupos(grupos, contactos_por_grupo):
    while True:
        print("LISTA DIGITAL DE CONTACTOS")
        print()
        print("ADMINISTRAR GRUPOS DE CONTACTOS")
        print("Eliminar grupos")
        print()
        nombre = input("Nombre del grupo (C para cancelar): ")
        if nombre == "C" or nombre == "c":
            return
        if nombre not in grupos:#Verificar si el grupo existe
            print("ESTE GRUPO NO ESTÁ REGISTRADO, NO SE PUEDE ELIMINAR")
            continue
        indice = grupos.index(nombre)#Buscar la posicion del grupo
        while True:
            opcion = input("OPCIÓN A-ACEPTAR C-CANCELAR: ")
            if opcion == "A" or opcion == "a":
                while True:
                    confirmar = input("CONFIRMA LA ELIMINACIÓN (SI/NO): ")
                    if confirmar == "SI" or confirmar == "si":
                        grupos.pop(indice)
                        contactos_por_grupo.pop(indice)
                        print("Grupo eliminado correctamente")
                        break
                    elif confirmar == "NO" or confirmar == "no":
                        print("Eliminación cancelada")
                        break
                    else:
                        print("Ingrese SI o NO")
                break
            elif opcion == "C" or opcion == "c":
                print("Eliminación cancelada")
                break
            else:
                print("Ingrese A o C")



#Opcion 4.5 Eliminar contactos de los grupos

def eliminar_contactos_grupos(grupos, contactos_por_grupo, contactos):
    while True:
        print("LISTA DIGITAL DE CONTACTOS")
        print()
        print("ADMINISTRAR GRUPOS DE CONTACTOS")
        print("Eliminar contactos de los grupos")
        print()
        nombre = input("Nombre del grupo (C para cancelar): ")
        if nombre == "C" or nombre == "c":
            return
        if nombre not in grupos: #Verificar si el grupo existe
            print("ESTE GRUPO NO EXISTE, NO PUEDE ELIMINARLE CONTACTOS")
            continue
        indice = grupos.index(nombre) #Buscar la posicion del grupo
        telefono = input("Teléfono: ")
        area = input("Área: ")
        if not telefono.isdigit() or not area.isdigit(): #Verificar que sean numeros
            print("EL TELÉFONO Y EL ÁREA DEBEN SER NUMÉRICOS")
            continue
        if len(telefono) < 5 or len(telefono) > 12:
            print("EL TELÉFONO DEBE TENER ENTRE 5 Y 12 DÍGITOS")
            continue
        telefono = int(telefono) #Convertir el telefono a entero
        area = int(area) #Convertir el area a entero
        if (telefono, area) not in contactos_por_grupo[indice]: #Verificar si pertenece al grupo
            print("ESTE CONTACTO NO EXISTE EN EL GRUPO, NO PUEDE ELIMINARLO")
            continue
        for contacto in contactos:
            if contacto[0] == telefono and contacto[1] == area:
                print("Nombre contacto:", contacto[3])
                break
        while True:
            opcion = input("OPCIÓN A-ACEPTAR C-CANCELAR: ")
            if opcion == "A" or opcion == "a":
                while True:
                    confirmar = input("CONFIRMA LA ELIMINACIÓN (SI/NO): ")
                    if confirmar == "SI" or confirmar == "si":
                        contactos_por_grupo[indice].remove((telefono, area))
                        print("Contacto eliminado del grupo correctamente")
                        break
                    elif confirmar == "NO" or confirmar == "no":
                        print("Eliminación cancelada")
                        break
                    else:
                        print("Ingrese SI o NO")
                break
            elif opcion == "C" or opcion == "c":
                print("Eliminación cancelada")
                break
            else:
                print("Ingrese A o C")
    


#4. Administrar grupos de contactos

def administrar_grupos(grupos, contactos_por_grupo, contactos):
    while True:
        print("LISTA DIGITAL DE CONTACTOS")
        print()
        print("ADMINISTRAR GRUPOS DE CONTACTOS")
        print("1. Agregar grupos")
        print("2. Agregar contactos a los grupos")
        print("3. Modificar grupos")
        print("4. Eliminar grupos")
        print("5. Eliminar contactos de los grupos")
        print("0. Fin")
        opcion = input("OPCIÓN: ")
        if opcion == "1":
            agregar_grupos(grupos, contactos_por_grupo)
        elif opcion == "2":
            agregar_contactos_grupos(grupos, contactos_por_grupo, contactos)
        elif opcion == "3":
            modificar_grupos(grupos, contactos_por_grupo)
        elif opcion == "4":
            eliminar_grupos(grupos, contactos_por_grupo)
        elif opcion == "5":
            eliminar_contactos_grupos(grupos, contactos_por_grupo, contactos)
        elif opcion == "0":
            break
        else:
            print("ESTA OPCIÓN NO EXISTE")



#Verificar si un dato cumple con el filtro
        
def cumple_filtro(dato, filtro):
    dato = str(dato).lower()#Convertir el dato a texto y minusculas
    filtro = filtro.lower()#Convertir el filtro a minusculas
    if filtro == "":#Si el filtro esta vacio, aceptar cualquier dato
        return True
    partes = filtro.split("%")#Separar el filtro donde aparece %
    if "%" not in filtro:#Si no hay %, comparar el texto completo
        return dato == filtro
    posicion = 0
    if filtro[0] != "%":
        if dato[:len(partes[0])] != partes[0]:
            return False
        posicion = len(partes[0])
        partes = partes[1:]
    for parte in partes:#Recorrer las partes del filtro
        if parte == "":#Ignorar las partes vacias
            continue
        indice = dato.find(parte, posicion)#Buscar la parte en el dato
        if indice == -1:#Si no se encuentra la parte
            return False
        posicion = indice + len(parte)#Continuar despues de la parte encontrada
    if filtro[0] != "%":#Verificar si el filtro no empieza con %
        inicio = filtro.split("%")[0]
        if dato[:len(inicio)] != inicio:
            return False
    if filtro[-1] != "%":
        final = filtro.split("%")[-1]
        if dato[len(dato) - len(final):] != final:
            return False
    return True#El dato cumple con el filtro
       


#Generar un archivo PDF con los contactos encontrados

def generar_pdf(resultados):
    pdf = SimpleDocTemplate("lista_contactos.pdf", pagesize=landscape(A3))
    estilos = getSampleStyleSheet()
    titulos = ["Nombre", "Teléfono", "Área", "Tipo", "Correo", "Dirección", "Fecha", "Pasatiempos", "Notas"]
    tabla_datos = [titulos]
    for contacto in resultados:
        datos = [contacto[3], contacto[0], contacto[1], contacto[2],
                 contacto[4], contacto[5], contacto[6], contacto[7], contacto[8]]
        fila = []
        for dato in datos:
            fila.append(Paragraph(escape(str(dato)), estilos["Normal"]))
        tabla_datos.append(fila)
    tabla = Table(tabla_datos, colWidths=[125, 80, 45, 45, 135, 180, 85, 180, 180], repeatRows=1)
    tabla.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.5, "black"),("VALIGN", (0, 0), (-1, -1), "TOP"),("FONTSIZE", (0, 0), (-1, 0), 9),("BACKGROUND", (0, 0), (-1, 0), "#DDDDDD"),]))
    pdf.build([tabla])
    


#5. Lista de contactos

def lista_contactos(contactos, grupos, contactos_por_grupo):#Mostrar y filtrar los contactos
    while True:#Repetir el menu hasta salir
        print("LISTA DIGITAL DE CONTACTOS")
        print()
        print("LISTA DE CONTACTOS")
        print()
        print("FILTROS:")
        nombre = input("Nombre contacto: ").lower()
        telefono = input("Teléfono: ")
        area = input("Área: ")
        fecha = input("Fecha de nacimiento: ")
        pasatiempos = input("Pasatiempos: ").lower()
        grupo = input("Grupo: ").lower()
        resultados = []#Guardar los contactos que cumplen los filtros
        for contacto in contactos:#Recorrer todos los contactos
            if not cumple_filtro(contacto[3], nombre):#Verificar el nombre
                continue#Pasar al siguiente contacto
            if not cumple_filtro(contacto[0], telefono):#Verificar el telefono
                continue#Pasar al siguiente contacto
            if not cumple_filtro(contacto[1], area):#Verificar el area
                continue#Pasar al siguiente contacto
            if not cumple_filtro(contacto[6], fecha):#Verificar la fecha de nacimiento
                continue#Pasar al siguiente contacto
            if not cumple_filtro(contacto[7], pasatiempos):#Verificar los pasatiempos
                continue#Pasar al siguiente contacto
            pertenece = False#Indicar si el contacto pertenece a un grupo
            if grupo == "":#Si no hay filtro de grupo
                pertenece = True
            else:#Si el usuario escribio un grupo
                for i in range(len(grupos)):#Recorrer los grupos
                    if cumple_filtro(grupos[i], grupo):#Verificar el nombre del grupo
                        if (contacto[0], contacto[1]) in contactos_por_grupo[i]:#Verificar si pertenece
                            pertenece = True#El contacto pertenece al grupo
                            break
            if pertenece:#Verificar si el contacto cumple el filtro de grupo
                resultados.append(contacto)#Guardar el contacto en los resultados
        print("Contactos encontrados:", len(resultados))#Mostrar la cantidad de contactos        
        while True:#Pedir confirmacion hasta que sea valida
            opcion = input("OPCIÓN A-ACEPTAR C-CANCELAR: ")
            if opcion == "A" or opcion == "a":#Aceptar la generacion de la lista
                print("Generando lista de contactos...")
                generar_pdf(resultados)  #Generar el PDF con los contactos encontrados
                break
            elif opcion == "C" or opcion == "c":#Cancelar la operacion
                print("Operación cancelada")
                break
            else:#Si la opcion no es valida
                print("Ingrese A o C")
        if opcion == "C" or opcion == "c":
            continue
        break



#7 Acerca de

def acerca_de():
    print("LISTA DIGITAL DE CONTACTOS")
    print()
    print("ACERCA DE")
    print()
    print("Nombre: Lista Digital de Contactos")
    print("Version: 1.0")
    print("Fecha de creacion: Octubre 2026")
    print("Autor: Frankie Cheng Zheng")
    input("Presione Enter para continuar...")


                
#Funcion principal
#Lista digital de contactos
                
def principal():
    areas = []
    configuracion = []
    contactos = []
    grupos = []
    contactos_por_grupo = []
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
                registrar_areas(areas,contactos,configuracion) 
            case "2":
                configurar_lista_contactos(areas,configuracion)
            case "3":
                registrar_contactos(contactos, areas, configuracion, grupos, contactos_por_grupo)
            case "4":
                administrar_grupos(grupos, contactos_por_grupo, contactos)
            case "5":
                lista_contactos(contactos, grupos, contactos_por_grupo)
            case "7":
                acerca_de()
                
            case "0":
                break
            case _:
                print("ESTA OPCIÓN NO EXISTE")
    print("FIN DEL PROGRAMA")
                             
principal()
