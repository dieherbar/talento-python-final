# Programa principal para la gestión de productos

import os
import funciones.auxiliares
from funciones.conectar_db import conectar_db

# ---------------------
# MENU PRINCIPAL
# ---------------------

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def pausar():
    input("\n Presioná Enter para continuar...")

def main():
    conexion = funciones.conectar_db.conectar_db()

    while True:
        limpiar_pantalla()
        print("\n" + "=" * 50)
        print("     SISTEMA DE GESTIÓN DE PRODUCTOS")
        print("=" * 50)
        print("  1. Agregar producto")
        print("  2. Ver todos los productos")
        print("  3. Buscar producto por nombre")
        print("  4. Eliminar producto")
        print("  5. Salir")
        print("-" * 50)

        opcion = input("Selecciona una opcion (1-5): ").strip()

        if opcion == "1":
            funciones.auxiliares.agregar_producto(conexion)
            pausar()
        elif opcion == "2":
            funciones.auxiliares.ver_productos(conexion)
            pausar()
        elif opcion == "3":
            funciones.auxiliares.buscar_productos(conexion)
            pausar()
        elif opcion == "4":
            funciones.auxiliares.eliminar_productos(conexion)
            pausar()
        elif opcion == "5":
            print("\n Gracias por usar el sistema. Hasta pronto!")
            break
        else:
            print(" Opcion invalida. Igresa un numero del 1 al 5")
            pausar()


    conexion.close()

if __name__ == "__main__":
    main()