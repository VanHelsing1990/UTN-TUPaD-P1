"""
Trabajo Práctico 6: Estructuras de datos complejas
Tecnicatura Universitaria en Programación a Distancia
"""

def ejercicio1():
    """Añadir nuevas frutas al diccionario"""
    print("--- Ejercicio 1 ---")
    precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
    
    # Añadir nuevas frutas
    precios_frutas['Naranja'] = 1200
    precios_frutas['Manzana'] = 1500
    precios_frutas['Pera'] = 2300
    
    print("Diccionario actualizado:", precios_frutas)
    return precios_frutas

def ejercicio2():
    """Actualizar precios existentes"""
    print("--- Ejercicio 2 ---")
    # Usar el diccionario del ejercicio 1
    precios_frutas = ejercicio1()
    
    precios_frutas['Banana'] = 1330
    precios_frutas['Manzana'] = 1700
    precios_frutas['Melón'] = 2800
    
    print("Diccionario con precios actualizados:", precios_frutas)
    return precios_frutas

def ejercicio3():
    """Crear lista solo con nombres de frutas"""
    print("--- Ejercicio 3 ---")
    # Usar el diccionario del ejercicio 2
    precios_frutas = ejercicio2()
    
    lista_frutas = list(precios_frutas.keys())
    print("Lista de frutas:", lista_frutas)
    return lista_frutas

def ejercicio4():
    """Agenda telefónica básica"""
    print("--- Ejercicio 4 ---")
    contactos = {}
    print("Cargando 5 contactos:")
    for i in range(5):
        nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
        numero = input(f"Ingrese el número de {nombre}: ")
        contactos[nombre] = numero
    
    consulta = input("\nIngrese un nombre para consultar: ")
    if consulta in contactos:
        print(f"Número de {consulta}: {contactos[consulta]}")
    else:
        print("Contacto no encontrado")
    
    return contactos

def ejercicio5():
    """Análisis de frecuencia de palabras"""
    print("--- Ejercicio 5 ---")
    frase = input("Ingrese una frase: ")
    palabras = frase.split()
    
    palabras_unicas = set(palabras)
    recuento = {}
    for palabra in palabras:
        recuento[palabra] = recuento.get(palabra, 0) + 1
    
    print("Palabras únicas:", palabras_unicas)
    print("Recuento:", recuento)
    return palabras_unicas, recuento

def ejercicio6():
    """Promedio de notas de alumnos"""
    print("--- Ejercicio 6 ---")
    alumnos = {}
    for i in range(3):
        nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
        print(f"Ingrese las 3 notas de {nombre}:")
        notas = tuple(float(input(f"Nota {j+1}: ")) for j in range(3))
        alumnos[nombre] = notas
    
    print("\nPromedios:")
    for nombre, notas in alumnos.items():
        promedio = sum(notas) / len(notas)
        print(f"Promedio de {nombre}: {promedio:.2f}")
    
    return alumnos

def ejercicio7():
    """Operaciones con conjuntos de estudiantes"""
    print("--- Ejercicio 7 ---")
    # Datos de ejemplo
    parcial1 = {'Ana', 'Luis', 'Carlos', 'Marta'}
    parcial2 = {'Luis', 'Marta', 'Pedro', 'Sofía'}
    
    print("Estudiantes que aprobaron Parcial 1:", parcial1)
    print("Estudiantes que aprobaron Parcial 2:", parcial2)
    print("Aprobaron ambos:", parcial1 & parcial2)
    print("Solo uno de los dos:", parcial1 ^ parcial2)
    print("Total de aprobados (al menos uno):", parcial1 | parcial2)
    
    return parcial1, parcial2

def ejercicio8():
    """Sistema de gestión de stock"""
    print("--- Ejercicio 8 ---")
    stock = {'Manzanas': 50, 'Naranjas': 30, 'Bananas': 40}
    print("Stock inicial:", stock)
    
    while True:
        print("\n--- Menú Stock ---")
        print("1. Consultar stock")
        print("2. Agregar unidades")
        print("3. Agregar nuevo producto")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            producto = input("Ingrese producto a consultar: ")
            if producto in stock:
                print(f"Stock de {producto}: {stock[producto]}")
            else:
                print("Producto no encontrado")
        
        elif opcion == "2":
            producto = input("Ingrese producto: ")
            if producto in stock:
                cantidad = int(input("Unidades a agregar: "))
                stock[producto] += cantidad
                print(f"Stock actualizado: {stock[producto]}")
            else:
                print("Producto no encontrado. Use opción 3 para agregar nuevo producto.")
        
        elif opcion == "3":
            producto = input("Ingrese nuevo producto: ")
            cantidad = int(input("Ingrese stock inicial: "))
            stock[producto] = cantidad
            print(f"Producto {producto} agregado con stock {cantidad}")
        
        elif opcion == "4":
            break
        
        else:
            print("Opción inválida")
    
    print("Stock final:", stock)
    return stock

def ejercicio9():
    """Agenda con tuplas como clave"""
    print("--- Ejercicio 9 ---")
    agenda = {
        ("lunes", "10:00"): "Reunión de equipo",
        ("martes", "15:00"): "Clase de inglés",
        ("jueves", "09:30"): "Médico",
        ("viernes", "14:00"): "Entrega de proyecto"
    }
    
    print("Agenda actual:")
    for (dia, hora), evento in agenda.items():
        print(f"{dia} {hora}: {evento}")
    
    while True:
        print("\n--- Consulta de Agenda ---")
        dia = input("Ingrese día (o 'salir' para terminar): ")
        if dia.lower() == 'salir':
            break
        
        hora = input("Ingrese hora (HH:MM): ")
        evento = agenda.get((dia.lower(), hora), "No hay eventos programados")
        print(f"Evento: {evento}")
    
    return agenda

def ejercicio10():
    """Invertir diccionario de países"""
    print("--- Ejercicio 10 ---")
    paises = {
        "Argentina": "Buenos Aires",
        "Chile": "Santiago",
        "Brasil": "Brasilia",
        "Uruguay": "Montevideo",
        "Paraguay": "Asunción"
    }
    
    print("Diccionario original:", paises)
    
    capitales = {capital: pais for pais, capital in paises.items()}
    print("Diccionario invertido:", capitales)
    
    return capitales

def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "="*50)
    print("TRABAJO PRÁCTICO 6 - ESTRUCTURAS DE DATOS COMPLEJAS")
    print("="*50)
    print("1. Ejercicio 1 - Añadir frutas al diccionario")
    print("2. Ejercicio 2 - Actualizar precios de frutas")
    print("3. Ejercicio 3 - Lista de frutas sin precios")
    print("4. Ejercicio 4 - Agenda telefónica")
    print("5. Ejercicio 5 - Análisis de frecuencia de palabras")
    print("6. Ejercicio 6 - Promedio de notas de alumnos")
    print("7. Ejercicio 7 - Operaciones con conjuntos")
    print("8. Ejercicio 8 - Sistema de gestión de stock")
    print("9. Ejercicio 9 - Agenda con tuplas")
    print("10. Ejercicio 10 - Invertir diccionario de países")
    print("0. Salir")
    print("="*50)

# Programa principal
def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione un ejercicio (1-10) o 0 para salir: ")
        
        if opcion == "0":
            print("¡Hasta luego!")
            break
        elif opcion == "1":
            ejercicio1()
        elif opcion == "2":
            ejercicio2()
        elif opcion == "3":
            ejercicio3()
        elif opcion == "4":
            ejercicio4()
        elif opcion == "5":
            ejercicio5()
        elif opcion == "6":
            ejercicio6()
        elif opcion == "7":
            ejercicio7()
        elif opcion == "8":
            ejercicio8()
        elif opcion == "9":
            ejercicio9()
        elif opcion == "10":
            ejercicio10()
        else:
            print("Opción inválida. Por favor, seleccione 1-10 o 0 para salir.")
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()
