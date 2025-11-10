import csv
import os
NOMBRE_ARCHIVO = "paises.csv"

def obtener_datos():
    
    lista_paises = []
        #Crea el archivo si no existe
    if not os.path.exists(NOMBRE_ARCHIVO):
        with open(NOMBRE_ARCHIVO, "w", newline="", encoding="utf_8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["nombre", "poblacion", "superficie", "continente"])
            #Escribe la primera fila del CSV, o sea, los encabezados
            escritor.writeheader()

            return lista_paises
    
    with open(NOMBRE_ARCHIVO, newline="", encoding="utf_8") as archivo:
        #Lee el formato csv interpreta las columnas
        lector = csv.DictReader(archivo)
        #Recorre y crea un diccionario y agregar cada diccionario a la lista
        for fila in lector:
            lista_paises.append({"nombre": fila["nombre"], "poblacion": int(fila["poblacion"]), "superficie": int(fila["superficie"]), "continente": fila["continente"] })

    return lista_paises
        

#FUNC PARA AGREGAR PAIS AL CSV
def agregar_pais_archivo(pais):
    with open(NOMBRE_ARCHIVO, "a", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["nombre", "poblacion", "superficie", "continente"])
        escritor.writerow(pais)


#Func para ingresar paises (1)
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


#FUNC PARA ACTUALZIAR DATOS (2)
def actualizar_datos():
    lista_paises = obtener_datos()
    print("Actualizar los datos de Poblacion y Superficie")
    nombre = input("Ingresa el nombre del pais que desee actualizar los datos").strip().lower()
    
    nombre_pais_encontrado = None

    for paises in lista_paises:
        if paises["nombre"].lower() == nombre.lower():
            nombre_pais_encontrado = nombre
            break

    if not nombre_pais_encontrado:
        print(f"Error: El pais '{nombre}' no fue encontrado.")
        return

    poblacion = input(f"Ingrese la poblacion de {nombre} que desea actualizar: ")
    
    while not validar_numero(poblacion):
        print("Error al ingresar la poblacion.")
        ejemplares = input(f"Ingrese la poblacion de {nombre} que desea actualizar: ")

    ejemplares = int(ejemplares)

    
# funcion para buscar paises (3)
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
        # mostrar resultados de la busqueda 
        print("\nResultados encontrados:")
        print("---------------------------")
        for pais in lista_resultado:
            print(f"Nombre: {pais['nombre'].capitalize()}")
            print(f"Población: {pais['poblacion']}")
            print(f"Superficie: {pais['superficie']}")
            print(f"Continente: {pais['continente'].capitalize()}")
            print("---------------------------")




# Función para filtrar países (4)
def filtrar_paises():
    print("\n------ Filtrar Países ------")
    print("1. Filtrar por continente")
    print("2. Filtrar por población mínima")
    print("3. Filtrar por superficie mínima")
    print("4. Volver al menú")

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

        if not validar_texto(continente):
            print("Error: El nombre no puede ser un número. Intente de nuevo.")
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

    for pais in lista_filtrada:
        print(f"Nombre: {pais['nombre'].capitalize()}")
        print(f"Población: {pais['poblacion']}")
        print(f"Superficie: {pais['superficie']}")
        print(f"Continente: {pais['continente'].capitalize()}")
        print("---------------------------")


# funcion para ordenar paises (5)
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
    

    total_paises = len(lista)
    total_poblacion = 0
    total_superficie = 0

    mayor_poblacion = lista[0]
    mayor_superficie = lista[0]
 
    for pais in lista:   # recorremos la lista para calcular mayores y totales
        total_poblacion += pais["poblacion"]
        total_superficie += pais["superficie"]

        if pais["poblacion"] > mayor_poblacion["poblacion"]:
            mayor_poblacion = pais

        if pais["superficie"] > mayor_superficie["superficie"]:
            mayor_superficie = pais
    # calculo de promedios
    promedio_poblacion = total_poblacion // total_paises
    promedio_superficie = total_superficie // total_paises

    print(f"Total de países: {total_paises}")
    print(f"Población total: {total_poblacion}")
    print(f"Población promedio: {promedio_poblacion}")
    print(f"Superficie total: {total_superficie} km²")
    print(f"Superficie promedio: {promedio_superficie} km²")
    print(f"País con mayor población: {mayor_poblacion['nombre'].capitalize()} ({mayor_poblacion['poblacion']})")
    print(f"País con mayor superficie: {mayor_superficie['nombre'].capitalize()} ({mayor_superficie['superficie']} km²)")



def existe_dato(dato):
    lista_paises = obtener_datos()

    for paises in lista_paises:
        if paises["nombre"].lower() == dato.strip().lower():
            return True
        
    return False


    #FUNC PARA VALIDAR NUMERO
def validar_numero(numero):
    numero = numero.strip()
    if numero.isdigit():
        numero = int(numero)
        return True
    
    return False


#FUNC PARA VALIDAR TEXTO
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


def mostrar_menu():
    while True:
        print("\n")
        print("******** MENU INFO PAISES ********")
        print("1 agregar un país")
        print("2 Actualizar datos de un país")
        print("3 Buscar un país")
        print("4 Filtrar países")
        print("5 Ordenar países")
        print("6 Mostrar estadísticas")
        print("7 Salir")
        print("*"*16)

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
                break#break()
            case __:
                print("La opcion seleccionada no es valida.")
mostrar_menu()