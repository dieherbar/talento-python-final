import sqlite3

conexion = sqlite3.connect("inventario.db")
# ---------------------
# Conexion y creacion de tabla
# ---------------------
def conectar_db():
    """ """
    #conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        categoria TEXT NOT NULL,
        precio REAL NOT NULL
        )
    """)
    conexion.commit()
    return conexion



