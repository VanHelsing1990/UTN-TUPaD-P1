# PRÁCTICA - ARCHIVOS - PROGRAMACIÓN 1
# ======================================

import os

# Función para cargar productos desde el archivo
def cargar_productos():
    productos = []
    if os.path.exists("productos.txt"):
        with open("productos.txt", "r") as archivo:
            for linea in archivo:
                linea_limpia = linea.strip()
                if linea_limpia:
                    datos = linea_limpia.split(",")
                    if len(datos) == 3:
                        producto = {
                            "nombre": datos[0],
                            "precio": float(datos[1]),
                            "cantidad": int(datos[2])
                        }
                        productos.append(producto)
    return productos

# Función para guardar productos en el archivo
def guardar_productos(productos):
    with open("productos.txt", "w") as archivo:
        for producto in productos:
            linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
            archivo.write(linea)

# Función para mostrar todos los productos
def mostrar_productos(productos):
    print("\n=== LISTA DE PRODUCTOS ===")
    if len(productos) == 0:
        print("No hay productos en el inventario")
    else:
        for producto in productos:
            print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")

# Función para agregar un nuevo producto
def agregar_producto(productos):
    print("\n=== AGREGAR NUEVO PRODUCTO ===")
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad en stock: "))
    
    nuevo_producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    productos.append(nuevo_producto)
    guardar_productos(productos)
    print("✅ Producto agregado correctamente")

# Función para buscar un producto por nombre
def buscar_producto(productos):
    print("\n=== BUSCAR PRODUCTO ===")
    if len(productos) == 0:
        print("No hay productos en el inventario")
        return
    
    nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
    
    encontrado = False
    for producto in productos:
        if producto["nombre"].lower() == nombre_buscar.lower():
            print(f"✅ Producto encontrado:")
            print(f"   Nombre: {producto['nombre']}")
            print(f"   Precio: ${producto['precio']}")
            print(f"   Cantidad: {producto['cantidad']}")
            encontrado = True
            break
    
    if not encontrado:
        print("❌ Producto no encontrado en el inventario")

# Función para mostrar el menú principal
def mostrar_menu():
    print("\n" + "="*40)
    print("          SISTEMA DE INVENTARIO")
    print("="*40)
    print("1. Mostrar todos los productos")
    print("2. Agregar nuevo producto")
    print("3. Buscar producto por nombre")
    print("4. Salir del programa")
    print("="*40)

# Programa principal
def main():
    # Cargar productos al iniciar el programa
    productos = cargar_productos()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == "1":
            mostrar_productos(productos)
        elif opcion == "2":
            agregar_producto(productos)
        elif opcion == "3":
            buscar_producto(productos)
        elif opcion == "4":
            print("\n=== PROGRAMA FINALIZADO ===")
            print("¡Gracias por usar el sistema de inventario!")
            break
        else:
            print("❌ Opción no válida. Por favor, seleccione 1, 2, 3 o 4.")
        
        # Pausa antes de mostrar el menú nuevamente
        input("\nPresione Enter para continuar...")

# Ejecutar el programa
if __name__ == "__main__":
    main()
