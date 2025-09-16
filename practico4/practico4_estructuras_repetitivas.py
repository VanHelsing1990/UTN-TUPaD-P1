# Ejercicio 1: Números del 0 al 100
print("Ejercicio 1:")
for i in range(0, 101):
    print(i)

# Ejercicio 2: Contar dígitos de un número
print("\nEjercicio 2:")
numero = input("Ingrese un número entero: ")
if numero.isdigit() or (numero[0] == '-' and numero[1:].isdigit()):
    print("Cantidad de dígitos:", len(numero) if numero[0] != '-' else len(numero) - 1)
else:
    print("Debe ingresar un número entero válido")

# Ejercicio 3: Suma entre dos números (excluyendo extremos)
print("\nEjercicio 3:")
try:
    inicio = int(input("Ingrese el número inicial: "))
    fin = int(input("Ingrese el número final: "))
    suma = sum(range(min(inicio, fin) + 1, max(inicio, fin)))
    print("La suma es:", suma)
except ValueError:
    print("Debe ingresar números enteros válidos")

# Ejercicio 4: Suma secuencial hasta 0
print("\nEjercicio 4:")
total = 0
while True:
    try:
        num = int(input("Ingrese un número (0 para terminar): "))
        if num == 0:
            break
        total += num
    except ValueError:
        print("Debe ingresar un número entero válido")
print("Total acumulado:", total)

# Ejercicio 5: Adivinar número aleatorio
print("\nEjercicio 5:")
import random
numero_secreto = random.randint(0, 9)
intentos = 0
while True:
    try:
        guess = int(input("Adivina el número (0-9): "))
        intentos += 1
        if guess == numero_secreto:
            print(f"¡Correcto! Intentos: {intentos}")
            break
        else:
            print("Incorrecto, intenta nuevamente")
    except ValueError:
        print("Debe ingresar un número entero válido")

# Ejercicio 6: Pares decrecientes (0-100)
print("\nEjercicio 6:")
for num in range(100, -1, -2):
    print(num)

# Ejercicio 7: Suma hasta número positivo
print("\nEjercicio 7:")
try:
    n = int(input("Ingrese un número entero positivo: "))
    if n < 0:
        print("Debe ser un número positivo")
    else:
        suma = sum(range(0, n + 1))
        print("La suma es:", suma)
except ValueError:
    print("Debe ingresar un número entero válido")

# Ejercicio 8: Estadísticas de 100 números
print("\nEjercicio 8:")
pares = impares = positivos = negativos = 0
for _ in range(100):
    while True:
        try:
            num = int(input("Ingrese un número entero: "))
            break
        except ValueError:
            print("Debe ingresar un número entero válido")
    
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

print(f"Pares: {pares}, Impares: {impares}")
print(f"Positivos: {positivos}, Negativos: {negativos}")

# Ejercicio 9: Media de 100 números
print("\nEjercicio 9:")
suma_total = 0
for _ in range(100):
    while True:
        try:
            num = int(input("Ingrese un número entero: "))
            break
        except ValueError:
            print("Debe ingresar un número entero válido")
    suma_total += num

print("Media:", suma_total / 100)

# Ejercicio 10: Invertir dígitos
print("\nEjercicio 10:")
try:
    numero = int(input("Ingrese un número entero: "))
    invertido = int(str(abs(numero))[::-1])
    if numero < 0:
        invertido *= -1
    print("Número invertido:", invertido)
except ValueError:
    print("Debe ingresar un número entero válido")
