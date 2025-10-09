"""
TRABAJO PRÁCTICO 6 - ESTRUCTURAS DE DATOS COMPLEJAS
Versión completamente funcional y corregida
"""

def ejercicio1():
    print("\n" + "="*50)
    print("EJERCICIO 1: Añadir frutas al diccionario")
    print("="*50)
    
    # Diccionario inicial
    precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
    print("Diccionario inicial:", precios_frutas)
    
    print("\nVamos a agregar 3 nuevas frutas:")
    for i in range(3):
        fruta = input(f"Nombre de la fruta {i+1}: ")
        try:
            precio = int(input(f"Precio de {fruta}: "))
            precios_frutas[fruta] = precio
        except ValueError:
            print("Precio inválido, se usará 0")
            precios_frutas[fruta] = 0
    
    print("\nDiccionario final:", precios_frutas)
    return precios_frutas

def ejercicio2():
    print("\n" + "="*50)
    print("EJERCICIO 2: Actualizar precios de frutas")
    print("="*50)
    
    # Usar datos del ejercicio 1 o crear nuevos
    precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450,
                     'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}
    
    print("Frutas disponibles:", list(precios_frutas.keys()))
    
    while True:
        print("\n--- Actualizar precios ---")
        print("Frutas disponibles:", list(precios_frutas.keys()))
        fruta = input("¿Qué fruta quieres actualizar? (o 'fin' para terminar): ")
        
        if fruta.lower() == 'fin':
            break
            
        if fruta in precios_frutas:
            try:
                nuevo_precio = int(input(f"Nuevo precio para {fruta}: "))
                precios_frutas[fruta] = nuevo_precio
                print(f"✅ {fruta} actualizada a ${nuevo_precio}")
            except ValueError:
                print("❌ Precio inválido")
        else:
            print("❌ Fruta no encontrada")
    
    print("\nDiccionario final:", precios_frutas)
    return precios_frutas

def ejercicio3():
    print("\n" + "="*50)
    print("EJERCICIO 3: Lista de frutas sin precios")
    print("="*50)
    
    precios_frutas = {'Banana': 1330, 'Ananá': 2500, 'Melón': 2800, 'Uva': 1450,
                     'Naranja': 1200, 'Manzana': 1700, 'Pera': 2300}
    
    print("Diccionario completo:", precios_frutas)
    
    lista_frutas = list(precios_frutas.keys())
    print("\nLista solo con nombres de frutas:", lista_frutas)
    
    return lista_frutas

def ejercicio4():
    print("\n" + "="*50)
    print("EJERCICIO 4: Agenda telefónica")
    print("="*50)
    
    contactos = {}
    print("Vamos a cargar contactos. Puedes escribir 'salir' en cualquier momento.")
    
    for i in range(5):
        nombre = input(f"\nNombre del contacto {i+1} (o 'salir' para terminar): ")
        
        if nombre.lower() == 'salir':
            print("Saliendo de la carga de contactos...")
            break
            
        numero = input(f"Teléfono de {nombre}: ")
        
        if numero.lower() == 'salir':
            print("Saliendo de la carga de contactos...")
            break
            
        contactos[nombre] = numero
        print(f"✅ Contacto '{nombre}' agregado")
    
    print(f"\nSe cargaron {len(contactos)} contactos")
    print("Agenda:", contactos)
    
    # Consultar contactos
    if contactos:
        print("\n--- CONSULTAS ---")
        while True:
            consulta = input("\n¿Qué contacto buscar? (o 'salir' para terminar): ")
            if consulta.lower() == 'salir':
                break
                
            if consulta in contactos:
                print(f"📞 {consulta}: {contactos[consulta]}")
            else:
                print("❌ Contacto no encontrado")
    
    return contactos

def ejercicio5():
    print("\n" + "="*50)
    print("EJERCICIO 5: Análisis de frecuencia de palabras")
    print("="*50)
    
    frase = input("Ingrese una frase: ")
    
    if not frase.strip():
        print("❌ No se ingresó ninguna frase")
        return set(), {}
    
    palabras = frase.split()
    
    # Palabras únicas usando set
    palabras_unicas = set(palabras)
    
    # Recuento de palabras
    recuento = {}
    for palabra in palabras:
        recuento[palabra] = recuento.get(palabra, 0) + 1
    
    print("\n--- RESULTADOS ---")
    print("Palabras únicas:", palabras_unicas)
    print("Recuento:", recuento)
    
    return palabras_unicas, recuento

def ejercicio6():
    print("\n" + "="*50)
    print("EJERCICIO 6: Promedio de notas de alumnos")
    print("="*50)
    
    alumnos = {}
    
    for i in range(3):
        print(f"\n--- Alumno {i+1} ---")
        nombre = input("Nombre del alumno (o 'salir' para terminar): ")
        
        if nombre.lower() == 'salir':
            print("Saliendo...")
            break
            
        notas = []
        for j in range(3):
            while True:
                try:
                    nota_texto = input(f"Nota {j+1} de {nombre} (o 'salir' para terminar): ")
                    if nota_texto.lower() == 'salir':
                        print("Saliendo...")
                        return alumnos
                    
                    nota = float(nota_texto)
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("❌ La nota debe estar entre 0 y 10")
                except ValueError:
                    print("❌ Error: Ingrese un número válido")
        
        alumnos[nombre] = tuple(notas)
    
    # Calcular promedios
    if alumnos:
        print("\n--- PROMEDIOS ---")
        for nombre, notas in alumnos.items():
            promedio = sum(notas) / len(notas)
            print(f"📊 {nombre}: {notas} -> Promedio: {promedio:.2f}")
    
    return alumnos

def ejercicio7():
    print("\n" + "="*50)
    print("EJERCICIO 7: Operaciones con conjuntos")
    print("="*50)
    
    # Datos de ejemplo más claros
    parcial1 = {'Ana', 'Luis', 'Carlos', 'Marta'}
    parcial2 = {'Luis', 'Marta', 'Pedro', 'Sofía'}
    
    print("ESTUDIANTES:")
    print("Parcial 1:", parcial1)
    print("Parcial 2:", parcial2)
    
    print("\n--- RESULTADOS ---")
    print("✅ Aprobaron ambos parciales:", parcial1 & parcial2)
    print("📝 Aprobaron solo uno:", parcial1 ^ parcial2)
    print("🎓 Aprobaron al menos uno:", parcial1 | parcial2)
    
    return parcial1, parcial2

def ejercicio8():
    print("\n" + "="*50)
    print("EJERCICIO 8: Sistema de gestión de stock")
    print("="*50)
    
    stock = {'Manzanas': 50, 'Naranjas': 30, 'Bananas': 40}
    print("Stock inicial:", stock)
    
    while True:
        print("\n" + "-"*30)
        print("MENÚ STOCK")
        print("-"*30)
        print("1. Consultar stock")
        print("2. Agregar unidades")
        print("3. Agregar producto nuevo")
        print("4. Ver todo el stock")
        print("5. Salir")
        
        opcion = input("\nSeleccione opción (1-5): ")
        
        if opcion == "1":
            producto = input("Producto a consultar: ")
            if producto in stock:
                print(f"Stock de {producto}: {stock[producto]}")
            else:
                print("❌ Producto no existe")
                
        elif opcion == "2":
            producto = input("Producto: ")
            if producto in stock:
                try:
                    cantidad = int(input("Unidades a agregar: "))
                    stock[producto] += cantidad
                    print(f"✅ Stock actualizado: {stock[producto]}")
                except ValueError:
                    print("❌ Cantidad inválida")
            else:
                print("❌ Producto no existe")
                
        elif opcion == "3":
            producto = input("Nuevo producto: ")
            try:
                cantidad = int(input("Stock inicial: "))
                stock[producto] = cantidad
                print(f"✅ Producto agregado: {producto} = {cantidad}")
            except ValueError:
                print("❌ Cantidad inválida")
                
        elif opcion == "4":
            print("\n--- STOCK COMPLETO ---")
            for producto, cantidad in stock.items():
                print(f"{producto}: {cantidad}")
                
        elif opcion == "5":
            break
            
        else:
            print("❌ Opción inválida")
    
    print("\nStock final:", stock)
    return stock

def ejercicio9():
    print("\n" + "="*50)
    print("EJERCICIO 9: Agenda con tuplas")
    print("="*50)
    
    agenda = {
        ("lunes", "10:00"): "Reunión de equipo",
        ("martes", "15:00"): "Clase de inglés",
        ("jueves", "09:30"): "Médico"
    }
    
    print("Agenda actual:")
    for (dia, hora), evento in agenda.items():
        print(f"📅 {dia} {hora}: {evento}")
    
    while True:
        print("\n--- CONSULTA ---")
        dia = input("Día (o 'salir' para terminar): ").lower()
        if dia == 'salir':
            break
            
        hora = input("Hora (HH:MM): ")
        
        evento = agenda.get((dia, hora), "❌ No hay eventos")
        print(f"Evento: {evento}")
    
    return agenda

def ejercicio10():
    print("\n" + "="*50)
    print("EJERCICIO 10: Invertir diccionario")
    print("="*50)
    
    paises = {
        "Argentina": "Buenos Aires",
        "Chile": "Santiago", 
        "Brasil": "Brasilia",
        "Uruguay": "Montevideo"
    }
    
    print("Diccionario original:")
    for pais, capital in paises.items():
        print(f"🇦🇷 {pais} -> {capital}")
    
    # Invertir
    invertido = {}
    for pais, capital in paises.items():
        invertido[capital] = pais
    
    print("\nDiccionario invertido:")
    for capital, pais in invertido.items():
        print(f"🏛️ {capital} -> {pais}")
    
    return invertido

def mostrar_menu():
    print("\n" + "="*60)
    print("TRABAJO PRÁCTICO 6 - MENÚ PRINCIPAL")
    print("="*60)
    print("1. Ejercicio 1 - Añadir frutas al diccionario")
    print("2. Ejercicio 2 - Actualizar precios de frutas") 
    print("3. Ejercicio 3 - Lista de frutas sin precios")
    print("4. Ejercicio 4 - Agenda telefónica")
    print("5. Ejercicio 5 - Análisis de frecuencia de palabras")
    print("6. Ejercicio 6 - Promedio de notas de alumnos")
    print("7. Ejercicio 7 - Operaciones con conjuntos")
    print("8. Ejercicio 8 - Sistema de gestión de stock")
    print("9. Ejercicio 9 - Agenda con tuplas")
    print("10. Ejercicio 10 - Invertir diccionario")
    print("0. SALIR")
    print("="*60)

def main():
    print("¡Bienvenido al Trabajo Práctico 6!")
    print("NOTA: En cualquier ejercicio puedes usar 'salir' para volver al menú")
    
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione un ejercicio (1-10) o 0 para salir: ").strip()
        
        if opcion == "0":
            print("¡Hasta luego! 👋")
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
            print("❌ Opción inválida. Por favor seleccione 1-10 o 0 para salir.")
        
        if opcion in "12345678910":
            input("\nPresione Enter para continuar...")

# Ejecutar el programa
if __name__ == "__main__":
    main()
