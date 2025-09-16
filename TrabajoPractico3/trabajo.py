# Práctico 3: Estructuras condicionales
# Tecnatura Universitaria en Programación - UTN a distancia

# ===== EJERCICIO 1 =====
# Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga "Es mayor de edad".

print("\n=== Ejercicio 1 ===")
edad = int(input("Por favor, ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")

# ===== EJERCICIO 2 =====
# Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6,
# deberá mostrar por pantalla un mensaje que diga "Aprobado"; en caso contrario deberá
# mostrar el mensaje "Desaprobado".

print("\n=== Ejercicio 2 ===")
nota = float(input("Por favor, ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# ===== EJERCICIO 3 =====
# Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par,
# imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir
# por pantalla "Por favor, ingrese un número par".

print("\n=== Ejercicio 3 ===")
numero = int(input("Por favor, ingrese un número par: "))
if numero % 2 == 0:  # El operador % devuelve el resto de la división
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# ===== EJERCICIO 4 =====
# Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# - Niño/a: menor de 12 años.
# - Adolescente: mayor o igual que 12 años y menor que 18 años.
# - Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# - Adulto/a: mayor o igual que 30 años.

print("\n=== Ejercicio 4 ===")
edad = int(input("Por favor, ingrese su edad: "))
if edad < 12:
    print("Niño/a")
elif 12 <= edad < 18:
    print("Adolescente")
elif 18 <= edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# ===== EJERCICIO 5 =====
# Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".

print("\n=== Ejercicio 5 ===")
contrasena = input("Por favor, ingrese una contraseña (8-14 caracteres): ")
longitud = len(contrasena)  # La función len() devuelve la longitud de un string
if 8 <= longitud <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# ===== EJERCICIO 6 =====
# Escribir un programa que tome una lista de números aleatorios, calcule su moda, mediana y media
# y determine si hay sesgo positivo, negativo o no hay sesgo.

print("\n=== Ejercicio 6 ===")
import random
from statistics import mode, median, mean

# Generar lista de 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular moda, mediana y media
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print(f"Lista generada: {numeros_aleatorios}")
print(f"Moda: {moda}, Mediana: {mediana}, Media: {media:.2f}")

# Determinar el tipo de sesgo
if media > mediana and mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("Sesgo negativo o a la izquierda")
else:
    print("Sin sesgo o sesgo no definido")

# ===== EJERCICIO 7 =====
# Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual.

print("\n=== Ejercicio 7 ===")
texto = input("Por favor, ingrese una frase o palabra: ")
vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"  # Incluye vocales con y sin acento

if texto and texto[-1] in vocales:  # Verificar que el texto no esté vacío y que su último carácter sea vocal
    texto += "!"
    
print(texto)

# ===== EJERCICIO 8 =====
# Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee para transformar su nombre.

print("\n=== Ejercicio 8 ===")
nombre = input("Por favor, ingrese su nombre: ")
print("Opciones disponibles:")
print("1. Nombre en mayúsculas")
print("2. Nombre en minúsculas")
print("3. Nombre con la primera letra mayúscula")

opcion = input("Seleccione una opción (1, 2 o 3): ")

if opcion == "1":
    resultado = nombre.upper()  # Convertir a mayúsculas
elif opcion == "2":
    resultado = nombre.lower()  # Convertir a minúsculas
elif opcion == "3":
    resultado = nombre.title()  # Primera letra de cada palabra en mayúscula
else:
    resultado = nombre
    print("Opción no válida. Se mostrará el nombre sin cambios.")

print(f"Resultado: {resultado}")

# ===== EJERCICIO 9 =====
# Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud según la escala de Richter e imprima el resultado por pantalla.

print("\n=== Ejercicio 9 ===")
magnitud = float(input("Por favor, ingrese la magnitud del terremoto: "))

if magnitud < 3:
    categoria = "Muy leve (imperceptible)"
elif 3 <= magnitud < 4:
    categoria = "Leve (ligeramente perceptible)"
elif 4 <= magnitud < 5:
    categoria = "Moderado (sentido por personas, pero generalmente no causa daños)"
elif 5 <= magnitud < 6:
    categoria = "Fuerte (puede causar daños en estructuras débiles)"
elif 6 <= magnitud < 7:
    categoria = "Muy Fuerte (puede causar daños significativos)"
else:
    categoria = "Extremo (puede causar graves daños a gran escala)"

print(f"Categoría: {categoria}")

# ===== EJERCICIO 10 =====
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S),
# qué mes del año es y qué día es, y determine la estación del año.

print("\n=== Ejercicio 10 ===")
hemisferio = input("¿En qué hemisferio se encuentra? (N para Norte, S para Sur): ").upper()
mes = int(input("¿Qué mes es? (1-12): "))
dia = int(input("¿Qué día es? (1-31): "))

# Determinar la estación según el hemisferio y la fecha
if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
    if hemisferio == "N":
        estacion = "Invierno"
    else:
        estacion = "Verano"
elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
    if hemisferio == "N":
        estacion = "Primavera"
    else:
        estacion = "Otoño"
elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
    if hemisferio == "N":
        estacion = "Verano"
    else:
        estacion = "Invierno"
else:  # Del 21 de septiembre al 20 de diciembre
    if hemisferio == "N":
        estacion = "Otoño"
    else:
        estacion = "Primavera"

print(f"La estación actual es: {estacion}")

print("\n=== Fin del programa ===")
