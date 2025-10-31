# =============================================
# PRÁCTICO 11: APLICACIÓN DE LA RECURSIVIDAD
# MENÚ PRINCIPAL DE EJERCICIOS
# =============================================

def mostrar_menu():
    """Función que muestra el menú de opciones"""
    print("\n" + "="*50)
    print("        MENÚ PRINCIPAL - RECURSIVIDAD")
    print("="*50)
    print("1. Factorial de números")
    print("2. Serie de Fibonacci")
    print("3. Potencia de un número")
    print("4. Conversión decimal a binario")
    print("5. Verificar palíndromo")
    print("6. Suma de dígitos")
    print("7. Pirámide de bloques")
    print("8. Contar dígitos en un número")
    print("0. Salir")
    print("="*50)

# =============================================
# EJERCICIO 1: FACTORIAL
# =============================================
def factorial(n):
    """Función recursiva que calcula el factorial de un número"""
    # Caso base: factorial de 0 o 1 es 1
    if n == 0 or n == 1:
        return 1
    # Caso recursivo: n * factorial(n-1)
    else:
        return n * factorial(n - 1)

def ejecutar_factorial():
    """Función que ejecuta el ejercicio del factorial"""
    print("\n--- EJERCICIO 1: FACTORIAL ---")
    try:
        n = int(input("Ingrese un número entero positivo: "))
        if n < 1:
            print("Por favor, ingrese un número positivo.")
            return
        
        print(f"\nFactoriales desde 1 hasta {n}:")
        for i in range(1, n + 1):
            resultado = factorial(i)
            print(f"Factorial de {i} = {resultado}")
    
    except ValueError:
        print("Error: Por favor ingrese un número válido.")

# =============================================
# EJERCICIO 2: FIBONACCI
# =============================================
def fibonacci(pos):
    """Función recursiva que calcula el valor Fibonacci en una posición"""
    # Casos base: posición 0 = 0, posición 1 = 1
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    # Caso recursivo: fib(n-1) + fib(n-2)
    else:
        return fibonacci(pos - 1) + fibonacci(pos - 2)

def ejecutar_fibonacci():
    """Función que ejecuta el ejercicio de Fibonacci"""
    print("\n--- EJERCICIO 2: SERIE FIBONACCI ---")
    try:
        n = int(input("Ingrese la posición máxima: "))
        if n < 0:
            print("Por favor, ingrese un número no negativo.")
            return
        
        print(f"\nSerie de Fibonacci hasta la posición {n}:")
        for i in range(n + 1):
            resultado = fibonacci(i)
            print(f"Posición {i}: {resultado}")
    
    except ValueError:
        print("Error: Por favor ingrese un número válido.")

# =============================================
# EJERCICIO 3: POTENCIA
# =============================================
def potencia(base, exp):
    """Función recursiva que calcula la potencia de un número"""
    # Caso base: cualquier número elevado a 0 es 1
    if exp == 0:
        return 1
    # Caso recursivo: base * potencia(base, exp-1)
    else:
        return base * potencia(base, exp - 1)

def ejecutar_potencia():
    """Función que ejecuta el ejercicio de potencia"""
    print("\n--- EJERCICIO 3: POTENCIA ---")
    try:
        base = int(input("Ingrese la base: "))
        exp = int(input("Ingrese el exponente: "))
        
        if exp < 0:
            print("Esta función solo maneja exponentes no negativos.")
            return
        
        resultado = potencia(base, exp)
        print(f"\nResultado: {base}^{exp} = {resultado}")
    
    except ValueError:
        print("Error: Por favor ingrese números válidos.")

# =============================================
# EJERCICIO 4: DECIMAL A BINARIO
# =============================================
def decimal_a_binario(n):
    """Función recursiva que convierte decimal a binario"""
    # Caso base: cuando el número es 0, retorna cadena vacía
    if n == 0:
        return ""
    # Caso recursivo: convierte el cociente y agrega el resto
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

def ejecutar_decimal_binario():
    """Función que ejecuta la conversión decimal a binario"""
    print("\n--- EJERCICIO 4: DECIMAL A BINARIO ---")
    try:
        numero = int(input("Ingrese un número decimal: "))
        if numero < 0:
            print("Por favor, ingrese un número positivo.")
            return
        
        resultado = decimal_a_binario(numero)
        # Si el resultado es vacío (número 0), mostramos "0"
        resultado_final = resultado if resultado else "0"
        print(f"El número {numero} en binario es: {resultado_final}")
    
    except ValueError:
        print("Error: Por favor ingrese un número válido.")

# =============================================
# EJERCICIO 5: PALÍNDROMO
# =============================================
def es_palindrome(palabra):
    """Función recursiva que verifica si una palabra es palíndromo"""
    # Casos base: cadena vacía o de 1 carácter siempre es palíndromo
    if len(palabra) <= 1:
        return True
    # Si los extremos son diferentes, no es palíndromo
    elif palabra[0] != palabra[-1]:
        return False
    # Caso recursivo: verifica el substring sin los extremos
    else:
        return es_palindrome(palabra[1:-1])

def ejecutar_palindromo():
    """Función que ejecuta la verificación de palíndromos"""
    print("\n--- EJERCICIO 5: PALÍNDROMO ---")
    palabra = input("Ingrese una palabra (sin espacios ni tildes): ").lower()
    
    # Remover espacios por si el usuario los ingresa
    palabra = palabra.replace(" ", "")
    
    resultado = es_palindrome(palabra)
    if resultado:
        print(f"'{palabra}' SÍ es un palíndromo")
    else:
        print(f"'{palabra}' NO es un palíndromo")

# =============================================
# EJERCICIO 6: SUMA DE DÍGITOS
# =============================================
def suma_digitos(n):
    """Función recursiva que suma los dígitos de un número"""
    # Caso base: cuando no hay más dígitos
    if n == 0:
        return 0
    # Caso recursivo: último dígito + suma del resto
    else:
        return (n % 10) + suma_digitos(n // 10)

def ejecutar_suma_digitos():
    """Función que ejecuta la suma de dígitos"""
    print("\n--- EJERCICIO 6: SUMA DE DÍGITOS ---")
    try:
        numero = int(input("Ingrese un número entero positivo: "))
        if numero < 0:
            print("Por favor, ingrese un número positivo.")
            return
        
        resultado = suma_digitos(numero)
        print(f"La suma de los dígitos de {numero} es: {resultado}")
    
    except ValueError:
        print("Error: Por favor ingrese un número válido.")

# =============================================
# EJERCICIO 7: PIRÁMIDE DE BLOQUES
# =============================================
def contar_bloques(n):
    """Función recursiva que calcula bloques totales en pirámide"""
    # Caso base: nivel 1 tiene 1 bloque
    if n == 1:
        return 1
    # Caso recursivo: bloques nivel actual + bloques niveles superiores
    else:
        return n + contar_bloques(n - 1)

def ejecutar_piramide_bloques():
    """Función que ejecuta el cálculo de bloques en pirámide"""
    print("\n--- EJERCICIO 7: PIRÁMIDE DE BLOQUES ---")
    try:
        nivel = int(input("Ingrese número de bloques en nivel base: "))
        if nivel < 1:
            print("Por favor, ingrese un número mayor a 0.")
            return
        
        resultado = contar_bloques(nivel)
        print(f"Total de bloques necesarios: {resultado}")
        
        # Mostrar la serie para mejor comprensión
        serie = " + ".join(str(i) for i in range(nivel, 0, -1))
        print(f"Desglose: {serie} = {resultado}")
    
    except ValueError:
        print("Error: Por favor ingrese un número válido.")

# =============================================
# EJERCICIO 8: CONTAR DÍGITOS
# =============================================
def contar_digito(numero, digito):
    """Función recursiva que cuenta apariciones de un dígito"""
    # Caso base: cuando no hay más dígitos
    if numero == 0:
        return 0
    # Si el último dígito coincide, suma 1 y continúa
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    # Si no coincide, continúa con el resto
    else:
        return contar_digito(numero // 10, digito)

def ejecutar_contar_digito():
    """Función que ejecuta el conteo de dígitos"""
    print("\n--- EJERCICIO 8: CONTAR DÍGITOS ---")
    try:
        num = int(input("Ingrese un número entero positivo: "))
        dig = int(input("Ingrese el dígito a contar (0-9): "))
        
        if num < 0:
            print("Por favor, ingrese un número positivo.")
            return
        
        if dig < 0 or dig > 9:
            print("Por favor, ingrese un dígito entre 0 y 9.")
            return
        
        resultado = contar_digito(num, dig)
        print(f"El dígito {dig} aparece {resultado} veces en el número {num}")
    
    except ValueError:
        print("Error: Por favor ingrese números válidos.")

# =============================================
# FUNCIÓN PRINCIPAL
# =============================================
def main():
    """Función principal que controla el flujo del programa"""
    print("BIENVENIDO AL SISTEMA DE EJERCICIOS DE RECURSIVIDAD")
    print("Este programa implementa 8 ejercicios usando recursión")
    
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (0-8): ")
        
        if opcion == "1":
            ejecutar_factorial()
        elif opcion == "2":
            ejecutar_fibonacci()
        elif opcion == "3":
            ejecutar_potencia()
        elif opcion == "4":
            ejecutar_decimal_binario()
        elif opcion == "5":
            ejecutar_palindromo()
        elif opcion == "6":
            ejecutar_suma_digitos()
        elif opcion == "7":
            ejecutar_piramide_bloques()
        elif opcion == "8":
            ejecutar_contar_digito()
        elif opcion == "0":
            print("\n¡Gracias por usar el sistema! ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Por favor seleccione 0-8.")
        
        input("\nPresione Enter para continuar...")

# =============================================
# EJECUCIÓN DEL PROGRAMA
# =============================================
if __name__ == "__main__":
    main()
