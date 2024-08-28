import sqlite3

# Conexión a la base de datos (se crea si no existe)
conexion = sqlite3.connect('managedbbussines.db')

# Crear un cursor para ejecutar comandos SQL
cursor = conexion.cursor()

# Crear tabla Unidad_medida
cursor.execute('''
CREATE TABLE IF NOT EXISTS Unidad_medida (
    unidad_medida_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_medida TEXT NOT NULL,
    tipo_medida TEXT NOT NULL
)
''')

# Crear tabla categoria_producto
cursor.execute('''
CREATE TABLE IF NOT EXISTS categoria_producto (
    categoria_prod_id INTEGER PRIMARY KEY AUTOINCREMENT,
    descripcion TEXT NOT NULL
)
''')

# Crear tabla servicios
cursor.execute('''
CREATE TABLE IF NOT EXISTS servicios (
    id_servicio INTEGER PRIMARY KEY AUTOINCREMENT,
    descripcion TEXT NOT NULL,
    unidad_medida_id INTEGER NOT NULL,
    cantidad REAL NOT NULL,
    precio REAL NOT NULL,
    FOREIGN KEY (unidad_medida_id) REFERENCES Unidad_medida(unidad_medida_id)
)
''')

# Crear tabla Inventarios
cursor.execute('''
CREATE TABLE IF NOT EXISTS Inventarios (
    id_inventario INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_producto TEXT NOT NULL,
    cantidad_prod REAL NOT NULL,
    fch_ingreso DATE NOT NULL,
    fecha_vencimiento_prod DATE,
    costo REAL NOT NULL,
    comentario TEXT,
    categoria_prod_id INTEGER NOT NULL,
    FOREIGN KEY (categoria_prod_id) REFERENCES categoria_producto(categoria_prod_id)
)
''')

# Crear tabla parametros
cursor.execute('''
CREATE TABLE IF NOT EXISTS parametros (
    id_parametro INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_parametro TEXT NOT NULL,
    valor_parametro TEXT NOT NULL,
    fch_registro DATE DEFAULT (DATE('now'))
)
''')

# Crear tabla factura
cursor.execute('''
CREATE TABLE IF NOT EXISTS factura (
    id_factura INTEGER PRIMARY KEY AUTOINCREMENT,
    descripcion TEXT NOT NULL,
    fch_factura DATE NOT NULL,
    total_pago REAL NOT NULL
)
''')

# Confirmar los cambios y cerrar la conexión
conexion.commit()
conexion.close()

print("Tablas creadas exitosamente en la base de datos.")
