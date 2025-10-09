"""
Trabajo Práctico 6: Estructuras de datos complejas
Tecnicatura Universitaria en Programación a Distancia
"""

# Ejercicio 1: Añadir nuevas frutas al diccionario
print("--- Ejercicio 1 ---")
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Añadir nuevas frutas
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print("Diccionario actualizado:", precios_frutas)

# Ejercicio 2: Actualizar precios existentes
print("\n--- Ejercicio 2 ---")
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print("Diccionario con precios actualizados:", precios_frutas)

# Ejercicio 3: Crear lista solo con nombres de frutas
print("\n--- Ejercicio 3 ---")
lista_frutas = list(precios_frutas.keys())
print("Lista de frutas:", lista_frutas)

# Ejercicio 4: Agenda telefónica básica
print("\n--- Ejercicio 4 ---")
contactos = {}
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input(f"Ingrese el número de {nombre}: ")
    contactos[nombre] = numero

consulta = input("\nIngrese un nombre para consultar: ")
if consulta in contactos:
    print(f"Número de {consulta}: {contactos[consulta]}")
else:
    print("Contacto no encontrado")

# Ejercicio 5: Análisis de frecuencia de palabras
print("\n--- Ejercicio 5 ---")
frase = input("Ingrese una frase: ")
palabras = frase.split()

palabras_unicas = set(palabras)
recuento = {}
for palabra in palabras:
    recuento[palabra] = recuento.get(palabra, 0) + 1

print("Palabras únicas:", palabras_unicas)
print("Recuento:", recuento)

# Ejercicio 6: Promedio de notas de alumnos
print("\n--- Ejercicio 6 ---")
alumnos = {}
for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    notas = tuple(float(input(f"Nota {j+1} de {nombre}: ")) for j in range(3))
    alumnos[nombre] = notas

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"Promedio de {nombre}: {promedio:.2f}")

# Ejercicio 7: Operaciones con conjuntos de estudiantes
print("\n--- Ejercicio 7 ---")
parcial1 = {'Ana', 'Luis', 'Carlos', 'Marta'}
parcial2 = {'Luis', 'Marta', 'Pedro', 'Sofía'}

print("Aprobaron ambos:", parcial1 & parcial2)
print("Solo uno de los dos:", parcial1 ^ parcial2)
print("Total de aprobados:", parcial1 | parcial2)

# Ejercicio 8: Sistema de gestión de stock
print("\n--- Ejercicio 8 ---")
stock = {'Manzanas': 50, 'Naranjas': 30, 'Bananas': 40}

while True:
    producto = input("\nIngrese producto (o 'salir' para terminar): ")
    if producto.lower() == 'salir':
        break
    
    if producto in stock:
        print(f"Stock actual: {stock[producto]}")
        cantidad = int(input("Unidades a agregar: "))
        stock[producto] += cantidad
    else:
        stock[producto] = int(input("Producto nuevo. Ingrese stock inicial: "))
    
    print("Stock actualizado:", stock)

# Ejercicio 9: Agenda con tuplas como clave
print("\n--- Ejercicio 9 ---")
agenda = {
    ("lunes", "10:00"): "Reunión de equipo",
    ("martes", "15:00"): "Clase de inglés",
    ("jueves", "09:30"): "Médico"
}

dia = input("Ingrese día: ")
hora = input("Ingrese hora (HH:MM): ")
evento = agenda.get((dia.lower(), hora), "No hay eventos programados")
print(f"Evento: {evento}")

# Ejercicio 10: Invertir diccionario de países
print("\n--- Ejercicio 10 ---")
paises = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Brasil": "Brasilia",
    "Uruguay": "Montevideo"
}

capitales = {capital: pais for pais, capital in paises.items()}
print("Diccionario invertido:", capitales)
