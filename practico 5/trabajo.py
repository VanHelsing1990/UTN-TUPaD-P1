# Ejercicio 1
print("=== Ejercicio 1 ===")
notas = [85, 92, 78, 90, 96, 88, 75, 83, 95, 80]
print("Lista de notas:", notas)
print("Promedio:", sum(notas)/len(notas))
print("Nota más alta:", max(notas))
print("Nota más baja:", min(notas))
print()

# Ejercicio 2
print("=== Ejercicio 2 ===")
productos = []
for i in range(5):
    productos.append(input(f"Ingrese producto {i+1}: "))
    
print("Lista ordenada:", sorted(productos))
eliminar = input("¿Qué producto desea eliminar? ")
if eliminar in productos:
    productos.remove(eliminar)
print("Lista actualizada:", productos)
print()

# Ejercicio 3
print("=== Ejercicio 3 ===")
numeros = [random.randint(1, 100) for _ in range(15)]
pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]
print("Números:", numeros)
print("Pares:", pares, "- Cantidad:", len(pares))
print("Impares:", impares, "- Cantidad:", len(impares))
print()

# Ejercicio 4
print("=== Ejercicio 4 ===")
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
sin_repetir = list(set(datos))
print("Original:", datos)
print("Sin repetir:", sin_repetir)
print()

# Ejercicio 5
print("=== Ejercicio 5 ===")
estudiantes = ["Ana", "Luis", "Marta", "Pedro", "Sofía", "Carlos", "Elena", "Diego"]
print("Lista inicial:", estudiantes)
accion = input("¿Agregar (a) o eliminar (e) estudiante? ").lower()

if accion == "a":
    nuevo = input("Nombre del nuevo estudiante: ")
    estudiantes.append(nuevo)
elif accion == "e":
    eliminar = input("Nombre del estudiante a eliminar: ")
    if eliminar in estudiantes:
        estudiantes.remove(eliminar)
print("Lista final:", estudiantes)
print()

# Ejercicio 6
print("=== Ejercicio 6 ===")
numeros = [1, 2, 3, 4, 5, 6, 7]
rotados = [numeros[-1]] + numeros[:-1]
print("Original:", numeros)
print("Rotada:", rotados)
print()

# Ejercicio 7
print("=== Ejercicio 7 ===")
temperaturas = [
    [15, 25],  # Lunes
    [14, 28],  # Martes
    [16, 30],  # Miércoles
    [13, 22],  # Jueves
    [12, 20],  # Viernes
    [11, 18],  # Sábado
    [10, 16]   # Domingo
]

minimas = [dia[0] for dia in temperaturas]
maximas = [dia[1] for dia in temperaturas]
amplitudes = [maxima - minima for minima, maxima in temperaturas]

print("Promedio mínimas:", sum(minimas)/len(minimas))
print("Promedio máximas:", sum(maximas)/len(maximas))
print("Día mayor amplitud:", amplitudes.index(max(amplitudes)) + 1)
print()

# Ejercicio 8
print("=== Ejercicio 8 ===")
notas_estudiantes = [
    [7, 8, 9],   # Estudiante 1
    [6, 7, 8],   # Estudiante 2
    [9, 9, 10],  # Estudiante 3
    [5, 6, 7],   # Estudiante 4
    [8, 7, 9]    # Estudiante 5
]

for i, estudiante in enumerate(notas_estudiantes, 1):
    print(f"Promedio estudiante {i}: {sum(estudiante)/len(estudiante):.2f}")

for j in range(3):
    materia_j = [estudiante[j] for estudiante in notas_estudiantes]
    print(f"Promedio materia {j+1}: {sum(materia_j)/len(materia_j):.2f}")
print()

# Ejercicio 9
print("=== Ejercicio 9 ===")
tablero = [["-"] * 3 for _ in range(3)]

def mostrar_tablero():
    for fila in tablero:
        print(" ".join(fila))

jugadores = ["X", "O"]
turno = 0
for _ in range(9):
    mostrar_tablero()
    fila = int(input("Fila (1-3): ")) - 1
    col = int(input("Columna (1-3): ")) - 1
    
    if tablero[fila][col] == "-":
        tablero[fila][col] = jugadores[turno]
        turno = 1 - turno
    else:
        print("Casilla ocupada")
    
mostrar_tablero()
print()

# Ejercicio 10
print("=== Ejercicio 10 ===")
ventas = [
    [10, 15, 12, 18, 20, 22, 25],  # Producto 1
    [5, 8, 10, 12, 15, 18, 20],    # Producto 2
    [12, 14, 16, 18, 20, 22, 24],  # Producto 3
    [8, 10, 12, 14, 16, 18, 20]    # Producto 4
]

totales_productos = [sum(producto) for producto in ventas]
totales_dias = [sum(dia) for dia in zip(*ventas)]

print("Total por producto:")
for i, total in enumerate(totales_productos, 1):
    print(f"Producto {i}: {total}")

print("Día con más ventas:", totales_dias.index(max(totales_dias)) + 1)
print("Producto más vendido:", totales_productos.index(max(totales_productos)) + 1)
