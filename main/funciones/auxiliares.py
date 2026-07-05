import sqlite3


def agregar_producto(conexion):
    """Pide datos al usuario y los guarda en la base de datos."""
    print("\n--- Nuevo producto")
    while True:
        nombre = input(" Nombre: ").strip()
        if nombre:
            break
        print("❌ El nombre no puede estar vacio")
    while True:
            categoria = input(" categoria: ").strip()
            if categoria:
                break
            print("❌ La categoria no puede estar vacia")
    while True:
        try:
            precio = float(input(" Precio: $").replace(",","."))
            if precio > 0:
                break
            print(" ❌ El precio debe ser mayor a 0 ")
        except ValueError:
            print(" ❌ Ingresa un numero valido (ej: 1200.40)")
    cursor = conexion.cursor()
    try:
        cursor.execute(
            "INSERT INTO productos (nombre,categoria,precio) VALUES (?,?,?) ",
            (nombre, categoria, precio),
        )
        conexion.commit()
        print(f" ✅ Producto '{nombre}' agregado correctamente.")
    except sqlite3.Error as e:
        conexion.rollback()
        print(f"\n ❌ Error al guardar: {e}")

def ver_productos(conexion):
    """Muestra todos os productos en formato tabla."""
    cursor = conexion.cursor()
    cursor.execute("SELECT id,nombre,categoria,precio FROM productos ORDER BY id")
    filas = cursor.fetchall()

    if not filas:
        print("\n no hay productos cargados.")
        return

    print("\n" + "-" * 60)
    print(f"  {'ID':<5} {'NOMBRE':<20} {'CATEGORÍA':<15} {'PRECIO':>15}")
    print("-" * 60)
    for id_, nombre, categoria, precio in filas:
        print(f"  {id_:<5} {nombre:<20} {categoria:<15} ${precio:>14,.2f}")
    print("-" * 60)
    print(f"  Total de productos: {len(filas)}")
  
def eliminar_productos(conexion):
    """Elimina productos por su id"""
    ver_productos(conexion)

    try:
        id_eliminar = int(input("\n Ingresa el ID del producto a eliminar: ").strip()) # 1
    except ValueError:
        print(" ❌ el id debe ser un numero entero")
        return

    cursor = conexion.cursor()
    cursor.execute("SELECT nombre FROM productos WHERE id = ? " , (id_eliminar,)) # id=1 nombre="coca-cola" cat="ada" precio=1231 -> ["1","coca-cola","categora",1231432]
    fila = cursor.fetchone()

    if not fila:
        print(f" ❌ No existe ningun producto con el id {id_eliminar}")
        return

    nombre = fila[0]
    print(f"\n Producto encontrado: {nombre}")
    respuesta = input(f" ¿ Confirmas que queres eliminar '{nombre}' (s/n): ").strip()
    if respuesta != 's':
        print("Operacion cancelada.")
        return

    try:
        cursor.execute("DELETE FROM productos WHERE id = ?",(id_eliminar,))
        conexion.commit()
        print(f"✅ producto '{nombre}' eliminado correctamente.")
    except sqlite3.Error as e:
        conexion.rollback()
        print(f"\n Error al eliminar: {e}")

def buscar_productos(conexion):
    """ Buscar productos por su nombre"""
    termino = input("\nIngresa el nombre a buscar: ").strip()
    if not termino:
        print(" ❌ El termino de busqueda no puede estar vacio")
        return

    cursor = conexion.cursor()
    cursor.execute("SELECT id,nombre,categoria,precio FROM productos WHERE nombre LIKE ? ORDER BY id", (f"%{termino}%",) )
    filas = cursor.fetchall()

    if not filas:
        print(f" No se encontraron los productos con este {termino}")
        return

    print(f"\n  Se encontraron {len(filas)} resultado(s):")
    for id_, nombre, categoria, precio in filas:
        print(f"    ID: {id_} | {nombre} | {categoria} | ${precio:,.2f}")
    