def consultar_inventario(inventario, producto):
    if producto in inventario:
        return f"{producto}: {inventario[producto]}"
    else:
        return f"El producto '{producto}' no se encuentra en el inventario."



def agregar_producto(inventario, producto, cantidad):
    if producto in inventario:
        inventario[producto] += cantidad
        print(f"Se han agregado {cantidad} unidades de '{producto}'. Ahora hay {inventario[producto]} en total.")
    else:
        inventario[producto] = cantidad
        print(f"El producto '{producto}' se ha añadido al inventario con {cantidad} unidades.")



def eliminar_producto(inventario, producto):
    if producto in inventario:
        del inventario[producto]
        print(f"El producto '{producto}' ha sido eliminado del inventario.")
    else:
        print(f"El producto '{producto}' no se encuentra en el inventario.")



def mostrar_inventario(inventario):
    print("Inventario actual:")
    if inventario:
        for producto, cantidad in sorted(inventario.items()):
            print(f"- {producto}: {cantidad}")
    else:
        print("El inventario está vacío.")



def main():
    # Inventario inicial
    inventario = {
        "manzanas": 50,
        "bananas": 30,
    }
    mostrar_inventario(inventario)

    while True:
        print("\nOpciones:")
        print("1. Consultar producto")
        print("2. Agregar producto")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            producto = input("Ingrese el nombre del producto que desea consultar: ")
            print(consultar_inventario(inventario, producto))

        elif opcion == "2":
            producto = input("Ingrese el nombre del producto que desea agregar: ")
            cantidad = int(input("Ingrese la cantidad que desea agregar: "))
            agregar_producto(inventario, producto, cantidad)

        elif opcion == "3":
            producto = input("Ingrese el nombre del producto que desea eliminar: ")
            eliminar_producto(inventario, producto)

        elif opcion == "4":
            mostrar_inventario(inventario)

        elif opcion == "5":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, elija una opción del 1 al 5.")

        mostrar_inventario(inventario)  # Mostrar inventario actualizado después de cada operación


# Ejecutar el programa principal
if __name__ == "__main__":
    main()
