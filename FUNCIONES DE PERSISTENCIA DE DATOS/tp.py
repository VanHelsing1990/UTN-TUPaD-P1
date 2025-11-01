import csv

# FUNCIONES DE PERSISTENCIA DE DATOS

def cargar_catalogo():
    """
    Carga el catálogo desde el archivo CSV al iniciar el programa.
    Si el archivo no existe, crea un catálogo con algunos libros de ejemplo.
    
    Returns:
        list: Lista de diccionarios con los libros del catálogo.
    """
    try:
        # Abre el archivo CSV en modo lectura
        with open('catalogo.csv', 'r', newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)  # Crea un lector de diccionarios
            catalogo = []
            # Itera sobre cada fila del CSV
            for fila in lector:
                # Convierte cada fila en un diccionario y agrega al catálogo
                catalogo.append({
                    'TITULO': fila['TITULO'],
                    'CANTIDAD': int(fila['CANTIDAD'])  # Convierte a entero
                })
            return catalogo
    except FileNotFoundError:
        # Si el archivo no existe, crea un catálogo con libros de ejemplo
        catalogo_ejemplo = [
            {'TITULO': 'Cien años de soledad', 'CANTIDAD': 3},
            {'TITULO': '1984', 'CANTIDAD': 2},
            {'TITULO': 'El principito', 'CANTIDAD': 0},
            {'TITULO': 'Don Quijote de la Mancha', 'CANTIDAD': 1},
            {'TITULO': 'Orgullo y prejuicio', 'CANTIDAD': 4}
        ]
        # Guarda el catálogo de ejemplo en el archivo CSV
        guardar_catalogo(catalogo_ejemplo)
        print("¡Bienvenido! Se ha creado un catálogo inicial con libros de ejemplo.")
        return catalogo_ejemplo


def guardar_catalogo(catalogo):
    """
    Guarda el catálogo actual en el archivo CSV.
    
    Args:
        catalogo (list): Lista de diccionarios con los libros a guardar.
    """
    # Abre el archivo CSV en modo escritura
    with open('catalogo.csv', 'w', newline='', encoding='utf-8') as archivo:
        campos = ['TITULO', 'CANTIDAD']  # Define las columnas del CSV
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()  # Escribe la fila de encabezado
        # Escribe cada libro del catálogo
        for libro in catalogo:
            escritor.writerow(libro)


# FUNCIONES DE VALIDACIÓN Y BÚSQUEDA

def normalizar_titulo(titulo):
    """
    Normaliza un título para comparaciones insensibles a mayúsculas y espacios.
    
    Args:
        titulo (str): Título a normalizar.
    
    Returns:
        str: Título normalizado (minúsculas, sin espacios extra).
    """
    # strip(): elimina espacios al inicio y final
    # split(): divide por espacios
    # join(): une con un solo espacio entre palabras
    # lower(): convierte a minúsculas
    return ' '.join(titulo.strip().split()).lower()


def buscar_libro(catalogo, titulo):
    """
    Busca un libro en el catálogo por título (comparación normalizada).
    
    Args:
        catalogo (list): Lista de diccionarios de libros.
        titulo (str): Título a buscar.
    
    Returns:
        tuple: (índice, libro) si se encuentra, (-1, None) si no.
    """
    titulo_normalizado = normalizar_titulo(titulo)
    # Itera sobre el catálogo con índice
    for i, libro in enumerate(catalogo):
        # Compara títulos normalizados
        if normalizar_titulo(libro['TITULO']) == titulo_normalizado:
            return i, libro  # Retorna índice y libro encontrado
    return -1, None  # Retorna -1 y None si no se encuentra


def validar_titulo(titulo):
    """
    Valida que un título no esté vacío después de normalizar.
    
    Args:
        titulo (str): Título a validar.
    
    Returns:
        bool: True si es válido, False si está vacío.
    """
    titulo_normalizado = normalizar_titulo(titulo)
    return len(titulo_normalizado) > 0


def validar_cantidad(cantidad_str):
    """
    Valida que una cadena represente un entero no negativo.
    
    Args:
        cantidad_str (str): Cadena a validar.
    
    Returns:
        bool: True si es un entero no negativo, False en caso contrario.
    """
    if cantidad_str.isdigit():  # Verifica si son solo dígitos
        cantidad = int(cantidad_str)
        return cantidad >= 0  # Verifica que sea no negativo
    return False


# FUNCIONES DE OPERACIONES DEL MENÚ

def ingresar_multiples_libros(catalogo):
    """
    Permite cargar varios libros al catálogo en una sola operación.
    
    Args:
        catalogo (list): Catálogo donde se agregarán los libros.
    """
    cantidad_libros_str = input("¿Cuántos libros desea ingresar? ")
    
    # Valida que sea un número positivo
    if not cantidad_libros_str.isdigit() or int(cantidad_libros_str) <= 0:
        print("Error: Debe ingresar un número entero positivo")
        return
    
    cantidad_libros = int(cantidad_libros_str)
    
    # Bucle para ingresar cada libro
    for i in range(cantidad_libros):
        print(f"\nLibro {i + 1}:")
        
        # Bucle para validar título
        while True:
            titulo = input("Título: ")
            if not validar_titulo(titulo):
                print("Error: El título no puede estar vacío")
                continue
            
            # Verifica que no exista duplicado
            idx, libro_existente = buscar_libro(catalogo, titulo)
            if libro_existente is not None:
                print("Error: Ya existe un libro con ese título")
                continue
            break  # Sale del bucle cuando el título es válido
        
        # Bucle para validar cantidad
        while True:
            cantidad_str = input("Cantidad disponible: ")
            if not validar_cantidad(cantidad_str):
                print("Error: La cantidad debe ser un entero no negativo")
                continue
            cantidad = int(cantidad_str)
            break  # Sale del bucle cuando la cantidad es válida
        
        # Agrega el nuevo libro al catálogo
        catalogo.append({
            'TITULO': titulo.strip(),  # Elimina espacios extra
            'CANTIDAD': cantidad
        })
        print("Libro agregado exitosamente")


def ingresar_ejemplares(catalogo):
    """
    Suma ejemplares a un título existente en el catálogo.
    
    Args:
        catalogo (list): Catálogo donde se actualizará el libro.
    """
    titulo = input("Ingrese el título del libro: ")
    
    # Busca el libro en el catálogo
    idx, libro = buscar_libro(catalogo, titulo)
    if libro is None:
        print("Error: No se encontró el libro en el catálogo")
        return
    
    # Bucle para validar cantidad a agregar
    while True:
        cantidad_str = input("Cantidad a agregar: ")
        if not validar_cantidad(cantidad_str):
            print("Error: La cantidad debe ser un entero no negativo")
            continue
        cantidad = int(cantidad_str)
        break
    
    # Actualiza la cantidad del libro
    libro['CANTIDAD'] += cantidad
    print(f"Se agregaron {cantidad} ejemplares. Nuevo total: {libro['CANTIDAD']}")


def mostrar_catalogo(catalogo):
    """
    Muestra todos los libros del catálogo con su stock actual.
    
    Args:
        catalogo (list): Catálogo a mostrar.
    """
    if not catalogo:  # Verifica si el catálogo está vacío
        print("El catálogo está vacío")
        return
    
    print("\nCatálogo completo:")
    print("-" * 40)  # Línea separadora
    # Itera y muestra cada libro
    for libro in catalogo:
        print(f"Título: {libro['TITULO']}")
        print(f"Ejemplares disponibles: {libro['CANTIDAD']}")
        print("-" * 40)


def listar_libros_existentes(catalogo):
    """
    Muestra solo los títulos de todos los libros en el catálogo.
    Útil para ver rápidamente qué libros están registrados.
    
    Args:
        catalogo (list): Catálogo a mostrar.
    """
    if not catalogo:  # Verifica si el catálogo está vacío
        print("El catálogo está vacío")
        return
    
    print("\nLista de todos los libros registrados:")
    print("-" * 40)
    # Itera y muestra solo los títulos
    for i, libro in enumerate(catalogo, 1):
        print(f"{i}. {libro['TITULO']}")
    print("-" * 40)
    print(f"Total de libros registrados: {len(catalogo)}")


def consultar_disponibilidad(catalogo):
    """
    Consulta y muestra la cantidad disponible de un libro específico.
    
    Args:
        catalogo (list): Catálogo donde buscar el libro.
    """
    titulo = input("Ingrese el título del libro: ")
    
    # Busca el libro en el catálogo
    idx, libro = buscar_libro(catalogo, titulo)
    if libro is None:
        print("Error: No se encontró el libro en el catálogo")
        return
    
    # Muestra la cantidad disponible
    print(f"Ejemplares disponibles de '{libro['TITULO']}': {libro['CANTIDAD']}")


def listar_agotados(catalogo):
    """
    Muestra solo los libros que tienen 0 ejemplares disponibles.
    
    Args:
        catalogo (list): Catálogo a analizar.
    """
    # List comprehension para filtrar libros agotados
    agotados = [libro for libro in catalogo if libro['CANTIDAD'] == 0]
    
    if not agotados:  # Verifica si hay libros agotados
        print("No hay libros agotados en el catálogo")
        return
    
    print("\nLibros agotados:")
    print("-" * 40)
    # Muestra cada libro agotado
    for libro in agotados:
        print(f"Título: {libro['TITULO']}")


def agregar_titulo(catalogo):
    """
    Agrega un único libro al catálogo con validación de duplicados.
    
    Args:
        catalogo (list): Catálogo donde se agregará el libro.
    """
    # Bucle para validar título
    while True:
        titulo = input("Título del libro: ")
        if not validar_titulo(titulo):
            print("Error: El título no puede estar vacío")
            continue
        
        # Verifica duplicados
        idx, libro_existente = buscar_libro(catalogo, titulo)
        if libro_existente is not None:
            print("Error: Ya existe un libro con ese título")
            continue
        break
    
    # Bucle para validar cantidad
    while True:
        cantidad_str = input("Cantidad disponible: ")
        if not validar_cantidad(cantidad_str):
            print("Error: La cantidad debe ser un entero no negativo")
            continue
        cantidad = int(cantidad_str)
        break
    
    # Agrega el nuevo libro al catálogo
    catalogo.append({
        'TITULO': titulo.strip(),
        'CANTIDAD': cantidad
    })
    print("Libro agregado exitosamente")


def actualizar_ejemplares(catalogo):
    """
    Realiza operaciones de préstamo (restar 1) o devolución (sumar 1) de ejemplares.
    
    Args:
        catalogo (list): Catálogo donde se actualizará el libro.
    """
    titulo = input("Ingrese el título del libro: ")
    
    # Busca el libro en el catálogo
    idx, libro = buscar_libro(catalogo, titulo)
    if libro is None:
        print("Error: No se encontró el libro en el catálogo")
        return
    
    print("\nOperaciones disponibles:")
    print("1. Préstamo (restar 1 ejemplar)")
    print("2. Devolución (sumar 1 ejemplar)")
    
    opcion = input("Seleccione una operación (1-2): ")
    
    # Procesa la opción seleccionada
    if opcion == '1':  # Préstamo
        if libro['CANTIDAD'] > 0:
            libro['CANTIDAD'] -= 1  # Resta un ejemplar
            print("Préstamo realizado exitosamente")
            print(f"Ejemplares restantes: {libro['CANTIDAD']}")
        else:
            print("Error: No hay ejemplares disponibles para préstamo")
    elif opcion == '2':  # Devolución
        libro['CANTIDAD'] += 1  # Suma un ejemplar
        print("Devolución realizada exitosamente")
        print(f"Ejemplares disponibles: {libro['CANTIDAD']}")
    else:
        print("Error: Opción no válida")


# FUNCIÓN PRINCIPAL Y MENÚ

def main():
    """
    Función principal del programa que controla el flujo de la aplicación.
    Muestra el menú principal y gestiona las opciones del usuario.
    """
    # Carga el catálogo desde el archivo al iniciar (con libros de ejemplo si es primera vez)
    catalogo = cargar_catalogo()
    
    # Bucle principal del menú
    while True:
        # Muestra las opciones del menú
        print("\n--- SISTEMA DE GESTIÓN DE BIBLIOTECA ---")
        print("1. Ingresar múltiples títulos")
        print("2. Ingresar ejemplares a título existente")
        print("3. Mostrar catálogo completo (con cantidades)")
        print("4. Listar libros existentes (solo títulos)")
        print("5. Consultar disponibilidad")
        print("6. Listar libros agotados")
        print("7. Agregar un título")
        print("8. Actualizar ejemplares (préstamo/devolución)")
        print("9. Salir")
        
        opcion = input("Seleccione una opción (1-9): ")
        
        # Procesa la opción seleccionada
        if opcion == '1':
            ingresar_multiples_libros(catalogo)
            guardar_catalogo(catalogo)  # Guarda cambios en CSV
        elif opcion == '2':
            ingresar_ejemplares(catalogo)
            guardar_catalogo(catalogo)  # Guarda cambios en CSV
        elif opcion == '3':
            mostrar_catalogo(catalogo)
        elif opcion == '4':
            listar_libros_existentes(catalogo)
        elif opcion == '5':
            consultar_disponibilidad(catalogo)
        elif opcion == '6':
            listar_agotados(catalogo)
        elif opcion == '7':
            agregar_titulo(catalogo)
            guardar_catalogo(catalogo)  # Guarda cambios en CSV
        elif opcion == '8':
            actualizar_ejemplares(catalogo)
            guardar_catalogo(catalogo)  # Guarda cambios en CSV
        elif opcion == '9':
            print("¡Hasta luego!")
            break  # Sale del bucle y termina el programa
        else:
            print("Error: Opción no válida. Por favor seleccione 1-9")


# PUNTO DE ENTRADA DEL PROGRAMA
if __name__ == "__main__":
    """
    Punto de entrada principal del programa.
    Esta condición verifica si el script se está ejecutando directamente
    (no importado como módulo) y en ese caso ejecuta la función main().
    """
    main()
