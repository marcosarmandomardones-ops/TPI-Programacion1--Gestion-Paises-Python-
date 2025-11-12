## Proyecto Integrador Programación I:
# Sistema de Gestión de Datos de Países en Python

# Descripción:
    # Este programa permite gestionar información de países utilizando un archivo CSV como base de datos. Incluye funciones para:
        #- Agregar países
        #- Actualizar datos
        #- Buscar por nombre
        #- Filtrar por distintos criterios
        #- Ordenar información
        #- Mostrar estadísticas generales

    #El programa utiliza un menú interactivo y validaciones para asegurar que los datos ingresados sean correctos.

# Autores: Pablo Mazuquin / Marcos Mardones
# Materia: Programación I
# Año: 2025

# ---------------------------------------------------
# Módulos importados
import csv
import os
NOMBRE_ARCHIVO = "paises.csv"

# FUNCION PARA OBTENER DATOS DEL CSV
def obtener_datos():
    
    lista_paises = []
        # Crea el archivo si no existe
    if not os.path.exists(NOMBRE_ARCHIVO):
        with open(NOMBRE_ARCHIVO, "w", newline="", encoding="utf_8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["nombre", "poblacion", "superficie", "continente"])
            # Escribe la primera fila del CSV, o sea, los encabezados
            escritor.writeheader()

            return lista_paises
    
    with open(NOMBRE_ARCHIVO, newline="", encoding="utf_8") as archivo:
        # Lee el formato csv interpreta las columnas
        lector = csv.DictReader(archivo)
        # Recorre y crea un diccionario y agregar cada diccionario a la lista
        for fila in lector:
            lista_paises.append({"nombre": fila["nombre"], "poblacion": int(fila["poblacion"]), "superficie": int(fila["superficie"]), "continente": fila["continente"] })

    return lista_paises
        

# FUNCION PARA AGREGAR PAIS AL ARCHIVO CSV
def agregar_pais_archivo(pais):
    with open(NOMBRE_ARCHIVO, "a", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["nombre", "poblacion", "superficie", "continente"])
        escritor.writerow(pais)


def guardar_lista_completa(lista_paises):
    """
    Sobrescribe el archivo CSV completo con la lista de países actualizada. Usa el modo 'w' (write).
    """
    # Definimos los encabezados
    headers = ["nombre", "poblacion", "superficie", "continente"]
    
    # Esto borra el contenido anterior y escribe el nuevo.
    with open(NOMBRE_ARCHIVO, 'w', newline='', encoding='utf-8') as archivo:
        
        escritor = csv.DictWriter(archivo, fieldnames=headers)
        # 1. Escribimos los encabezados
        escritor.writeheader()
        
        # 2. Escribimos todas las filas de la lista
        # (writerows es como writerow pero para una lista de dic)
        escritor.writerows(lista_paises)


# FUNCION PARA INGRESAR PAIS (1)
def ingresar_pais():
    while True:
        print("\n")
        print("------ INGRESA UN PAIS ------")
        nombre = input("Ingrese el nombre del pais:  ").strip()

        #Comprueba si el pais ya existe
        if existe_dato(nombre):
            print("Este pais ya fue agregado previamente.")
            continue # Vuelve al inicio del while  
    
        if nombre == "":
            print("Error al ingresar el pais")
            continue

        nombre = nombre.lower()
        
        if not validar_texto(nombre):
            print("Error: El nombre no puede ser un número. Intente de nuevo.")
            continue

        poblacion = input("Ingrese su poblacion: ").strip()
        #Comprueba que sea un numero valido
        if not validar_numero(poblacion):
            print("Error al ingresar el numero de poblacion")
            continue

        poblacion = int(poblacion)

        superficie = input("Ingrese su superficie: ").strip()


        if not validar_numero(superficie):
            print("Error al ingresar la superficie")
            continue

        superficie = int(superficie)

        continente = input("Ingrese el continente del pais:  ").strip()
    
        if continente == "":
            print("Error al ingresar el continente")
            continue

        if not validar_texto(continente):
            print("Error: El nombre no puede ser un número. Intente de nuevo.")
            continue

        continente = continente.lower()
        break

    agregar_pais_archivo({"nombre": nombre, "poblacion": poblacion, "superficie": superficie, "continente": continente })
    print("| Lista de paises actualizada! |")


# FUNCION PARA ACTUALIZAR DATOS DE UN PAIS (2)
def actualizar_datos():
    lista_paises = obtener_datos()

    if not lista_paises: # Comprueba si la lista está vacía
        print("No hay países cargados para actualizar.")
        return
    
    print("Actualizar los datos de Poblacion y Superficie")
    nombre_buscado = input("Ingresa el nombre del pais que desee actualizar los datos: ").strip().lower()
    
    pais_encontrado = None
    indice_pais = -1

    # Usamos enumerate para obtener el índice (i) y el país (pais)
    for i, pais in enumerate(lista_paises): 
        if pais["nombre"].lower() == nombre_buscado:
            pais_encontrado = pais
            indice_pais = i
            break # Encontramos el país, salimos del 'for'

    if not pais_encontrado:
            print(f"Error: El pais '{nombre_buscado}' no fue encontrado.")
            return # Volvemos al menú

    print(f"\nDatos actuales de {pais_encontrado['nombre'].capitalize()}:")
    print(f"  Población: {pais_encontrado['poblacion']}")
    print(f"  Superficie: {pais_encontrado['superficie']}")

# Pedir nueva población (con validación)
    nueva_poblacion_str = input(f"Ingrese la NUEVA población: ").strip()
    while not validar_numero(nueva_poblacion_str):
        print("Error al ingresar la poblacion.")
        nueva_poblacion_str = input(f"Ingrese la NUEVA población: ").strip()

    # Pedir nueva superficie (con validación)
    nueva_superficie_str = input(f"Ingrese la NUEVA superficie: ").strip()
    while not validar_numero(nueva_superficie_str):
        print("Error al ingresar la superficie.")
        nueva_superficie_str = input(f"Ingrese la NUEVA superficie: ").strip()

    # Convertir a enteros
    nueva_poblacion = int(nueva_poblacion_str)
    nueva_superficie = int(nueva_superficie_str)

    #Modificar el diccionario DENTRO de la lista
    lista_paises[indice_pais]["poblacion"] = nueva_poblacion
    lista_paises[indice_pais]["superficie"] = nueva_superficie

    #Guardar la lista COMPLETA en el CSV
    guardar_lista_completa(lista_paises) 
    print(f"\n¡Datos de {pais_encontrado['nombre'].capitalize()} actualizados exitosamente!")

    
# FUNCION PARA BUSCAR PAIS (3)
def buscar_paises():
    print("\n------ Buscar Países ------")
    nombre_pais = input("Ingrese parte o el nombre completo del país: ").strip().lower()
    
    if nombre_pais == "":
        print("Error al ingresar el nombre del país")
        return
    
    lista_paises = obtener_datos()
    lista_resultado = []

    # Recorremos la lista de paises
    for pais in lista_paises:
        nombre = pais["nombre"].lower()

        if nombre_pais in nombre:   # por coincidencia parcial
            lista_resultado.append(pais)
    
    if len(lista_resultado) == 0:
        print("No se encontraron resultados en la búsqueda")
        return
    else:
        # Mostrar resultados de la búsqueda
        print("\nResultados encontrados:")
        print("---------------------------")
        for pais in lista_resultado:
            print(f"Nombre: {pais['nombre'].capitalize()}")
            print(f"Población: {pais['poblacion']}")
            print(f"Superficie: {pais['superficie']}")
            print(f"Continente: {pais['continente'].capitalize()}")
            print("---------------------------")


# FUNCION PARA FILTRAR PAISES (4)
def filtrar_paises():
    print("\n------ Filtrar Países ------")
    print("1. Filtrar por continente")
    print("2. Filtrar por población mínima")
    print("3. Filtrar por superficie mínima")
    print("4. Volver al menú")
    # Selección de opción
    opcion_filtro = input("Seleccione una opción: ").strip()

    lista_paises = obtener_datos()
    lista_filtrada = []

    # filtar por continente 
    if opcion_filtro == "1":
        continente = input("Ingrese el continente: ").strip().lower()

        if continente == "":
            print("Error al ingresar el continente")
            return

        for pais in lista_paises:
            if pais["continente"].lower() == continente:
                lista_filtrada.append(pais)

    # filtrar por poblción minima
    elif opcion_filtro == "2":
        poblacion = input("Ingrese población mínima: ").strip()

        if not validar_numero(poblacion):
            print("Error al ingresar un número no válido")
            return

        poblacion = int(poblacion)

        for pais in lista_paises:
            if pais["poblacion"] >= poblacion:
                lista_filtrada.append(pais)

    # filtrar por superficie minima
    elif opcion_filtro == "3":
        superficie = input("Ingrese superficie mínima: ").strip()

        if not validar_numero(superficie):
            print("Error al ingresar un número no válido")
            return

        superficie = int(superficie)

        for pais in lista_paises:
            if pais["superficie"] >= superficie:
                lista_filtrada.append(pais)

    # Volver al menú
    elif opcion_filtro == "4":
        return
    else:
        print("Opción no válida")
        return

    if len(lista_filtrada) == 0:
        print("No se encontraron países")
        return

    print("\nPaíses filtrados:")
    print("---------------------------")
    # Mostrar países filtados
    for pais in lista_filtrada:
        print(f"Nombre: {pais['nombre'].capitalize()}")
        print(f"Población: {pais['poblacion']}")
        print(f"Superficie: {pais['superficie']}")
        print(f"Continente: {pais['continente'].capitalize()}")
        print("---------------------------")


# FUNCION PARA ORDENAR PAISES (5)
def ordenar_paises():
    print("\n------ Ordenar Países ------")
    print("1. Ordenar por nombre (A-Z)")
    print("2. Ordenar por población (menor a mayor)")
    print("3. Ordenar por superficie (menor a mayor)")
    print("4. Volver al menú")

    opcion = input("Seleccione una opción: ").strip()
    if opcion not in ["1", "2", "3", "4"]:
        print("Error: Opcion invalida")
        return
    
    if opcion == "4":
        print("Redirigiendo al Menu de Opciones.")
        return
    
    lista = obtener_datos()
    long_lista = len(lista)

    # Ciclo para ordenar 
    for i in range(long_lista):
        for j in range(long_lista - 1):
            
            if opcion == "1":  #nombre
                if lista[j]["nombre"] > lista[j + 1]["nombre"]:
                    temporal = lista[j]
                    lista[j] = lista[j + 1]
                    lista[j + 1] = temporal
            
            elif opcion == "2":  #población
                if lista[j]["poblacion"] > lista[j + 1]["poblacion"]:
                    temporal = lista[j]
                    lista[j] = lista[j + 1]
                    lista[j + 1] = temporal
            
            elif opcion == "3":  # superficie
                if lista[j]["superficie"] > lista[j + 1]["superficie"]:
                    temporal = lista[j]
                    lista[j] = lista[j + 1]
                    lista[j + 1] = temporal

    # Mostrar ordenados
    print("\nPaíses ordenados:")
    print("---------------------------")

    # Mostrar países ordenados
    for pais in lista:
        print(f"Nombre: {pais['nombre'].capitalize()}")
        print(f"Población: {pais['poblacion']}")
        print(f"Superficie: {pais['superficie']} km²")
        print(f"Continente: {pais['continente'].capitalize()}")
        print("---------------------------")


# funcion para mostrar estadisticas (6)
def mostrar_estadisticas():
    print("\n------ Estadísticas de Países ------")
    lista = obtener_datos()

    if len(lista) == 0:
        print("No encontramos países registrados")
        return
    
    # Inicializamos variables
    total_paises = len(lista)
    total_poblacion = 0
    total_superficie = 0

    mayor_poblacion = lista[0]
    mayor_superficie = lista[0]
    # Recorremos la lista para calcular mayores y totales
    for pais in lista:   
        total_poblacion += pais["poblacion"]
        total_superficie += pais["superficie"]

        if pais["poblacion"] > mayor_poblacion["poblacion"]:
            mayor_poblacion = pais

        if pais["superficie"] > mayor_superficie["superficie"]:
            mayor_superficie = pais

    #  Calculas promedios
    promedio_poblacion = total_poblacion // total_paises
    promedio_superficie = total_superficie // total_paises

    print(f"Total de países: {total_paises}")
    print(f"Población total: {total_poblacion}")
    print(f"Población promedio: {promedio_poblacion}")
    print(f"Superficie total: {total_superficie} km²")
    print(f"Superficie promedio: {promedio_superficie} km²")
    print(f"País con mayor población: {mayor_poblacion['nombre'].capitalize()} ({mayor_poblacion['poblacion']})")
    print(f"País con mayor superficie: {mayor_superficie['nombre'].capitalize()} ({mayor_superficie['superficie']} km²)")


# VERIFICAR SI EL PAIS YA EXISTE
def existe_dato(dato):
    lista_paises = obtener_datos()

    for paises in lista_paises:
        if paises["nombre"].lower() == dato.strip().lower():
            return True  
    return False


    # VALIDAR NUMEROS
def validar_numero(numero):
    numero = numero.strip()
    if numero.isdigit():
        numero = int(numero)
        return True
    
    return False

# VALIDAR TEXTOS
def validar_texto(texto):
    """
    Valida que el texto no esté vacío y que no sea un número.
    Devuelve True si es un texto válido, False si está vacío o es un número.
    """
    texto_limpio = texto.strip() # Limpia espacios al inicio y final
    
    # 1. Revisa si el texto quedó vacío
    if not texto_limpio:
        return False
    # 2. Revisa si el texto limpio son SOLO números
    if texto_limpio.isdigit():
        return False
    # 3. Si pasó las dos pruebas, es un texto válido
    return True

# MENU PRINCIPAL
def mostrar_menu():
    while True:
        print("\n")
        print("******** MENU INFO PAISES ********")
        print("1 Agregar un país")
        print("2 Actualizar datos de un país")
        print("3 Buscar un país")
        print("4 Filtrar países")
        print("5 Ordenar países")
        print("6 Mostrar estadísticas")
        print("7 Salir")
        print("*"*16)

        # Leer opción del usuario
        opcion_menu = input("Ingrese una opcion: ").strip()
        match opcion_menu:
            case "1":
                ingresar_pais()
            case "2":
                actualizar_datos()
            case "3":
                buscar_paises()
            case "4":
                filtrar_paises()
            case "5":
                ordenar_paises()
            case "6":
                mostrar_estadisticas()
            case "7":
                print("Saliendo del sistema. ¡Gracias por usar el programa!")
                break
            case __:
                print("La opcion seleccionada no es valida.")
mostrar_menu()