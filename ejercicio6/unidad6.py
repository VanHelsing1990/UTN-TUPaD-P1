# Práctico 2: Funciones en Python
# Tecnnicatura Universitaria en Programación a Distancia
# Programación I

# ===== EJERCICIO 1 =====
def imprimir_hola_mundo():
    """Función que imprime 'Hola Mundo!' por pantalla"""
    print("Hola Mundo!")

# ===== EJERCICIO 2 =====
def saludar_usuario(nombre):
    """Función que recibe un nombre y devuelve un saludo personalizado"""
    return f"Hola {nombre}!"

# ===== EJERCICIO 3 =====
def informacion_personal(nombre, apellido, edad, residencia):
    """Función que recibe datos personales y los imprime formateados"""
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# ===== EJERCICIO 4 =====
def calcular_area_circulo(radio):
    """Función que calcula el área de un círculo dado su radio"""
    import math
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    """Función que calcula el perímetro de un círculo dado su radio"""
    import math
    return 2 * math.pi * radio

# ===== EJERCICIO 5 =====
def segundos_a_horas(segundos):
    """Función que convierte segundos a horas"""
    return segundos / 3600

# ===== EJERCICIO 6 =====
def tabla_multiplicar(numero):
    """Función que imprime la tabla de multiplicar de un número del 1 al 10"""
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# ===== EJERCICIO 7 =====
def operaciones_basicas(a, b):
    """Función que realiza las 4 operaciones básicas y devuelve una tupla"""
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por cero"
    return suma, resta, multiplicacion, division

# ===== EJERCICIO 8 =====
def calcular_imc(peso, altura):
    """Función que calcula el Índice de Masa Corporal (IMC)"""
    return peso / (altura ** 2)

# ===== EJERCICIO 9 =====
def celsius_a_fahrenheit(celsius):
    """Función que convierte grados Celsius a Fahrenheit"""
    return (celsius * 9/5) + 32

# ===== EJERCICIO 10 =====
def calcular_promedio(a, b, c):
    """Función que calcula el promedio de tres números"""
    return (a + b + c) / 3

# ===== PROGRAMA PRINCIPAL =====
def main():
    """Función principal que ejecuta todos los ejercicios"""
    
    print("=== EJERCICIO 1 ===")
    imprimir_hola_mundo()
    
    print("\n=== EJERCICIO 2 ===")
    nombre = input("Ingrese su nombre: ")
    print(saludar_usuario(nombre))
    
    print("\n=== EJERCICIO 3 ===")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = input("Ingrese su edad: ")
    residencia = input("Ingrese su lugar de residencia: ")
    informacion_personal(nombre, apellido, edad, residencia)
    
    print("\n=== EJERCICIO 4 ===")
    radio = float(input("Ingrese el radio del círculo: "))
    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)
    print(f"Área del círculo: {area:.2f}")
    print(f"Perímetro del círculo: {perimetro:.2f}")
    
    print("\n=== EJERCICIO 5 ===")
    segundos = int(input("Ingrese la cantidad de segundos: "))
    horas = segundos_a_horas(segundos)
    print(f"{segundos} segundos equivalen a {horas:.2f} horas")
    
    print("\n=== EJERCICIO 6 ===")
    numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
    tabla_multiplicar(numero)
    
    print("\n=== EJERCICIO 7 ===")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultados = operaciones_basicas(num1, num2)
    print(f"Suma: {resultados[0]}")
    print(f"Resta: {resultados[1]}")
    print(f"Multiplicación: {resultados[2]}")
    print(f"División: {resultados[3]}")
    
    print("\n=== EJERCICIO 8 ===")
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))
    imc = calcular_imc(peso, altura)
    print(f"Su Índice de Masa Corporal (IMC) es: {imc:.2f}")
    
    print("\n=== EJERCICIO 9 ===")
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    fahrenheit = celsius_a_fahrenheit(celsius)
    print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")
    
    print("\n=== EJERCICIO 10 ===")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))
    promedio = calcular_promedio(num1, num2, num3)
    print(f"El promedio de {num1}, {num2} y {num3} es: {promedio:.2f}")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
