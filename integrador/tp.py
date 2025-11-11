"""
TRABAJO PRÁCTICO INTEGRADOR - GESTIÓN DE DATOS DE PAÍSES
Tecnicatura Universitaria en Programación a Distancia
Programación 1

"""

import csv
import os

# =============================================================================
# FUNCIONES DE VALIDACIÓN
# =============================================================================

def validar_entero(mensaje):
    """Valida que se ingrese un número entero positivo"""
    while True:
        valor = input(mensaje).strip()
        if valor == "":
            print("❌ Error: Este campo no puede estar vacío.")
            continue
        if valor.isdigit():
            numero = int(valor)
            if numero >= 0:
                return numero
            else:
                print("❌ Error: El número debe ser positivo.")
        else:
            print("❌ Error: Debe ingresar un número entero válido.")

def validar_texto(mensaje):
    """Valida que se ingrese texto no vacío"""
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        else:
            print("❌ Error: Este campo no puede estar vacío.")

def validar_entero_opcional(mensaje):
    """Valida números enteros opcionales (pueden estar vacíos)"""
    while True:
        valor = input(mensaje).strip()
        if valor == "":
            return None
        if valor.isdigit():
            return int(valor)
        else:
            print("❌ Error: Debe ingresar un número entero válido o dejar vacío.")

# =============================================================================
# FUNCIONES DE ARCHIVO
# =============================================================================

def crear_archivo_si_no_existe(nombre_archivo):
    """Crea el archivo CSV si no existe"""
    if not os.path.exists(nombre_archivo):
        with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["nombre", "poblacion", "superficie", "continente"])
            escritor.writeheader()
        print("✓ Se ha creado el archivo paises.csv")

def cargar_paises(nombre_archivo):
    """Carga los países desde el archivo CSV"""
    paises = []
    if not os.path.exists(nombre_archivo):
        return paises

    with open(nombre_archivo, "r", newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            # Validar que los campos necesarios existan y sean válidos
            if (fila["nombre"] and 
                fila["poblacion"].isdigit() and 
                fila["superficie"].isdigit() and 
                fila["continente"]):
                
                pais = {
                    "nombre": fila["nombre"],
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"]
                }
                paises.append(pais)
    
    print(f"✓ Datos cargados: {len(paises)} países")
    return paises

def guardar_paises(nombre_archivo, paises):
    """Guarda los países en el archivo CSV"""
    with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["nombre", "poblacion", "superficie", "continente"])
        escritor.writeheader()
        for pais in paises:
            escritor.writerow(pais)
    print("✓ Datos guardados correctamente")

# =============================================================================
# FUNCIONES AUXILIARES
# =============================================================================

def mostrar_lista_paises(paises, titulo="LISTA DE PAÍSES"):
    """Muestra una lista de países formateada"""
    if not paises:
        print("❌ No hay países para mostrar.")
        return
    
    print(f"\n{titulo}")
    print("-" * 70)
    print(f"{'NOMBRE':<20} {'POBLACIÓN':<15} {'SUPERFICIE':<15} {'CONTINENTE':<15}")
    print("-" * 70)
    
    for pais in paises:
        print(f"{pais['nombre']:<20} {pais['poblacion']:<15,} {pais['superficie']:<15,} {pais['continente']:<15}")
    
    print("-" * 70)
    print(f"Total: {len(paises)} países")

def pais_existe(paises, nombre):
    """Verifica si un país ya existe en la lista"""
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            return True
    return False

# =============================================================================
# FUNCIONALIDADES PRINCIPALES
# =============================================================================

def agregar_pais(nombre_archivo):
    """Agrega un nuevo país a la base de datos"""
    print("\n" + "="*50)
    print("AGREGAR NUEVO PAÍS")
    print("="*50)
    
    # Cargar países existentes
    paises = cargar_paises(nombre_archivo)
    
    nombre = validar_texto("Nombre del país: ")
    
    # Verificar si el país ya existe
    if pais_existe(paises, nombre):
        print("❌ Este país ya existe en la base de datos.")
        return
    
    poblacion = validar_entero("Población: ")
    superficie = validar_entero("Superficie (km²): ")
    continente = validar_texto("Continente: ")
    
    # Crear nuevo país
    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    
    paises.append(nuevo_pais)
    guardar_paises(nombre_archivo, paises)
    print(f"✓ País '{nombre}' agregado correctamente")

def buscar_pais(nombre_archivo):
    """Busca países por nombre (coincidencia parcial)"""
    print("\n" + "="*50)
    print("BUSCAR PAÍS")
    print("="*50)
    
    paises = cargar_paises(nombre_archivo)
    
    if not paises:
        print("❌ No hay países en la base de datos.")
        return
    
    consulta = validar_texto("Ingrese el nombre o parte del nombre: ").lower()
    resultados = []
    
    for pais in paises:
        if consulta in pais["nombre"].lower():
            resultados.append(pais)
    
    if resultados:
        mostrar_lista_paises(resultados, f"RESULTADOS DE BÚSQUEDA: '{consulta}'")
    else:
        print("❌ No se encontraron países con ese nombre.")

def actualizar_pais(nombre_archivo):
    """Actualiza los datos de un país existente"""
    print("\n" + "="*50)
    print("ACTUALIZAR PAÍS")
    print("="*50)
    
    paises = cargar_paises(nombre_archivo)
    
    if not paises:
        print("❌ No hay países en la base de datos.")
        return
    
    nombre = validar_texto("Ingrese el nombre exacto del país a actualizar: ")
    pais_encontrado = None
    
    # Buscar el país
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            pais_encontrado = pais
            break
    
    if not pais_encontrado:
        print(f"❌ No se encontró el país '{nombre}'.")
        return
    
    # Mostrar datos actuales
    print(f"\nDatos actuales de {pais_encontrado['nombre']}:")
    print(f"  Población: {pais_encontrado['poblacion']:,}")
    print(f"  Superficie: {pais_encontrado['superficie']:,} km²")
    print(f"  Continente: {pais_encontrado['continente']}")
    
    print("\nIngrese los nuevos datos (deje vacío para mantener el actual):")
    
    # Actualizar población
    nueva_poblacion = validar_entero_opcional("Nueva población: ")
    if nueva_poblacion is not None:
        pais_encontrado["poblacion"] = nueva_poblacion
    
    # Actualizar superficie
    nueva_superficie = validar_entero_opcional("Nueva superficie (km²): ")
    if nueva_superficie is not None:
        pais_encontrado["superficie"] = nueva_superficie
    
    # Actualizar continente
    nuevo_continente = input("Nuevo continente: ").strip()
    if nuevo_continente:
        pais_encontrado["continente"] = nuevo_continente
    
    guardar_paises(nombre_archivo, paises)
    print(f"✓ País '{pais_encontrado['nombre']}' actualizado correctamente")

def filtrar_por_continente(nombre_archivo):
    """Filtra países por continente"""
    print("\n" + "="*50)
    print("FILTRAR POR CONTINENTE")
    print("="*50)
    
    paises = cargar_paises(nombre_archivo)
    
    if not paises:
        print("❌ No hay países en la base de datos.")
        return
    
    continente = validar_texto("Ingrese el continente: ").lower()
    resultados = []
    
    for pais in paises:
        if pais["continente"].lower() == continente:
            resultados.append(pais)
    
    if resultados:
        mostrar_lista_paises(resultados, f"PAÍSES EN {continente.upper()}")
    else:
        print(f"❌ No hay países en el continente '{continente}'.")

def filtrar_por_rango_poblacion(nombre_archivo):
    """Filtra países por rango de población"""
    print("\n" + "="*50)
    print("FILTRAR POR RANGO DE POBLACIÓN")
    print("="*50)
    
    paises = cargar_paises(nombre_archivo)
    
    if not paises:
        print("❌ No hay países en la base de datos.")
        return
    
    print("Ingrese el rango de población:")
    minimo = validar_entero("Población mínima: ")
    maximo = validar_entero("Población máxima: ")
    
    resultados = []
    for pais in paises:
        if minimo <= pais["poblacion"] <= maximo:
            resultados.append(pais)
    
    if resultados:
        mostrar_lista_paises(resultados, f"PAÍSES CON POBLACIÓN {minimo:,} - {maximo:,}")
    else:
        print("❌ No hay países en ese rango de población.")

def filtrar_por_rango_superficie(nombre_archivo):
    """Filtra países por rango de superficie"""
    print("\n" + "="*50)
    print("FILTRAR POR RANGO DE SUPERFICIE")
    print("="*50)
    
    paises = cargar_paises(nombre_archivo)
    
    if not paises:
        print("❌ No hay países en la base de datos.")
        return
    
    print("Ingrese el rango de superficie:")
    minimo = validar_entero("Superficie mínima (km²): ")
    maximo = validar_entero("Superficie máxima (km²): ")
    
    resultados = []
    for pais in paises:
        if minimo <= pais["superficie"] <= maximo:
            resultados.append(pais)
    
    if resultados:
        mostrar_lista_paises(resultados, f"PAÍSES CON SUPERFICIE {minimo:,} - {maximo:,} km²")
    else:
        print("❌ No hay países en ese rango de superficie.")

def mostrar_todos_paises(nombre_archivo):
    """Muestra todos los países"""
    print("\n" + "="*50)
    print("TODOS LOS PAÍSES")
    print("="*50)
    
    paises = cargar_paises(nombre_archivo)
    mostrar_lista_paises(paises)

def ordenar_paises(nombre_archivo):
    """Ordena países por diferentes criterios"""
    print("\n" + "="*50)
    print("ORDENAR PAÍSES")
    print("="*50)
    
    paises = cargar_paises(nombre_archivo)
    
    if not paises:
        print("❌ No hay países en la base de datos.")
        return
    
    print("1. Ordenar por nombre (A-Z)")
    print("2. Ordenar por nombre (Z-A)")
    print("3. Ordenar por población (ascendente)")
    print("4. Ordenar por población (descendente)")
    print("5. Ordenar por superficie (ascendente)")
    print("6. Ordenar por superficie (descendente)")
    
    opcion = input("Seleccione una opción (1-6): ").strip()
    
    paises_ordenados = paises.copy()
    n = len(paises_ordenados)
    
    # Ordenamiento burbuja
    for i in range(n - 1):
        for j in range(n - i - 1):
            cambiar = False
            
            if opcion == '1':  # Nombre A-Z
                if paises_ordenados[j]["nombre"] > paises_ordenados[j + 1]["nombre"]:
                    cambiar = True
            elif opcion == '2':  # Nombre Z-A
                if paises_ordenados[j]["nombre"] < paises_ordenados[j + 1]["nombre"]:
                    cambiar = True
            elif opcion == '3':  # Población ascendente
                if paises_ordenados[j]["poblacion"] > paises_ordenados[j + 1]["poblacion"]:
                    cambiar = True
            elif opcion == '4':  # Población descendente
                if paises_ordenados[j]["poblacion"] < paises_ordenados[j + 1]["poblacion"]:
                    cambiar = True
            elif opcion == '5':  # Superficie ascendente
                if paises_ordenados[j]["superficie"] > paises_ordenados[j + 1]["superficie"]:
                    cambiar = True
            elif opcion == '6':  # Superficie descendente
                if paises_ordenados[j]["superficie"] < paises_ordenados[j + 1]["superficie"]:
                    cambiar = True
            else:
                print("❌ Opción no válida.")
                return
            
            if cambiar:
                # Intercambiar elementos
                temp = paises_ordenados[j]
                paises_ordenados[j] = paises_ordenados[j + 1]
                paises_ordenados[j + 1] = temp
    
    # Mostrar resultados ordenados
    criterios = {
        '1': 'nombre (A-Z)',
        '2': 'nombre (Z-A)',
        '3': 'población (ascendente)',
        '4': 'población (descendente)',
        '5': 'superficie (ascendente)',
        '6': 'superficie (descendente)'
    }
    
    if opcion in criterios:
        mostrar_lista_paises(paises_ordenados, f"PAÍSES ORDENADOS POR {criterios[opcion].upper()}")

def mostrar_estadisticas(nombre_archivo):
    """Muestra estadísticas de los países"""
    print("\n" + "="*50)
    print("ESTADÍSTICAS")
    print("="*50)
    
    paises = cargar_paises(nombre_archivo)
    
    if not paises:
        print("❌ No hay países en la base de datos.")
        return
    
    # Inicializar variables
    pais_max_poblacion = paises[0]
    pais_min_poblacion = paises[0]
    pais_max_superficie = paises[0]
    pais_min_superficie = paises[0]
    suma_poblacion = 0
    suma_superficie = 0
    continentes = {}
    
    # Calcular estadísticas
    for pais in paises:
        # Población
        if pais["poblacion"] > pais_max_poblacion["poblacion"]:
            pais_max_poblacion = pais
        if pais["poblacion"] < pais_min_poblacion["poblacion"]:
            pais_min_poblacion = pais
        suma_poblacion += pais["poblacion"]
        
        # Superficie
        if pais["superficie"] > pais_max_superficie["superficie"]:
            pais_max_superficie = pais
        if pais["superficie"] < pais_min_superficie["superficie"]:
            pais_min_superficie = pais
        suma_superficie += pais["superficie"]
        
        # Continentes
        continente = pais["continente"]
        if continente in continentes:
            continentes[continente] += 1
        else:
            continentes[continente] = 1
    
    # Calcular promedios
    promedio_poblacion = suma_poblacion / len(paises)
    promedio_superficie = suma_superficie / len(paises)
    
    # Mostrar resultados
    print(f"📊 Total de países: {len(paises)}")
    print("\n👥 POBLACIÓN:")
    print(f"   • Mayor población: {pais_max_poblacion['nombre']} ({pais_max_poblacion['poblacion']:,})")
    print(f"   • Menor población: {pais_min_poblacion['nombre']} ({pais_min_poblacion['poblacion']:,})")
    print(f"   • Promedio: {promedio_poblacion:,.0f}")
    
    print("\n🗺️  SUPERFICIE:")
    print(f"   • Mayor superficie: {pais_max_superficie['nombre']} ({pais_max_superficie['superficie']:,} km²)")
    print(f"   • Menor superficie: {pais_min_superficie['nombre']} ({pais_min_superficie['superficie']:,} km²)")
    print(f"   • Promedio: {promedio_superficie:,.0f} km²")
    
    print("\n🌍 DISTRIBUCIÓN POR CONTINENTE:")
    for continente, cantidad in continentes.items():
        print(f"   • {continente}: {cantidad} país(es)")

# =============================================================================
# MENÚS
# =============================================================================

def menu_filtrar(nombre_archivo):
    """Submenú para filtros"""
    while True:
        print("\n" + "="*50)
        print("FILTRAR PAÍSES")
        print("="*50)
        print("1. Por continente")
        print("2. Por rango de población")
        print("3. Por rango de superficie")
        print("4. Volver al menú principal")
        print("="*50)
        
        opcion = input("Seleccione una opción (1-4): ").strip()
        
        if opcion == '1':
            filtrar_por_continente(nombre_archivo)
        elif opcion == '2':
            filtrar_por_rango_poblacion(nombre_archivo)
        elif opcion == '3':
            filtrar_por_rango_superficie(nombre_archivo)
        elif opcion == '4':
            break
        else:
            print("❌ Opción no válida.")
        
        input("\nPresione Enter para continuar...")

def menu_principal():
    """Menú principal del programa"""
    nombre_archivo = "paises.csv"
    crear_archivo_si_no_existe(nombre_archivo)
    
    while True:
        print("\n" + "="*60)
        print(" SISTEMA DE GESTIÓN DE DATOS DE PAÍSES")
        print("="*60)
        print("1. 📋 Mostrar todos los países")
        print("2. ➕ Agregar nuevo país")
        print("3. ✏️  Actualizar datos de país")
        print("4. 🔍 Buscar país por nombre")
        print("5. 📊 Filtrar países")
        print("6. 📈 Ordenar países")
        print("7. 📊 Mostrar estadísticas")
        print("8. 🚪 Salir")
        print("="*60)
        
        opcion = input("Seleccione una opción (1-8): ").strip()
        
        if opcion == '1':
            mostrar_todos_paises(nombre_archivo)
        elif opcion == '2':
            agregar_pais(nombre_archivo)
        elif opcion == '3':
            actualizar_pais(nombre_archivo)
        elif opcion == '4':
            buscar_pais(nombre_archivo)
        elif opcion == '5':
            menu_filtrar(nombre_archivo)
        elif opcion == '6':
            ordenar_paises(nombre_archivo)
        elif opcion == '7':
            mostrar_estadisticas(nombre_archivo)
        elif opcion == '8':
            print("\n¡Gracias por usar el Sistema de Gestión de Países! 👋")
            break
        else:
            print("❌ Opción no válida. Por favor, seleccione 1-8.")
        
        input("\nPresione Enter para continuar...")

# =============================================================================
# PROGRAMA PRINCIPAL
# =============================================================================

if __name__ == "__main__":
    menu_principal()
