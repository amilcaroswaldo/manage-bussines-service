from sqlalchemy import Column, Integer, String, ForeignKey,NUMERIC
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UnidadMedida(Base):
    __tablename__ = "Unidad_medida"
    
    unidad_medida_id = Column(Integer, primary_key=True, autoincrement=True)
    nombre_medida = Column(String, nullable=False)
    tipo_medida = Column(String, nullable=False)

class CategoriaProducto(Base):
    __tablename__ = "categoria_producto"
    
    categoria_prod_id = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String, nullable=False)

class Servicios(Base):
    __tablename__ = "servicios"
    
    id_servicio = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String, nullable=False)
    unidad_medida_id = Column(Integer, ForeignKey('Unidad_medida.unidad_medida_id'), nullable=False)
    cantidad = Column(Integer, nullable=False)
    precio = Column(NUMERIC, nullable=False)

class Inventarios(Base):
    __tablename__ = "Inventarios"
    
    id_inventario = Column(Integer, primary_key=True, autoincrement=True)
    nombre_producto = Column(String, nullable=False)
    cantidad_prod = Column(NUMERIC, nullable=False)
    fch_ingreso = Column(String, nullable=False)  # Cambia a DATE si es necesario
    fecha_vencimiento_prod = Column(String)  # Cambia a DATE si es necesario
    costo = Column(NUMERIC, nullable=False)
    comentario = Column(String)
    categoria_prod_id = Column(Integer, ForeignKey('categoria_producto.categoria_prod_id'), nullable=False)

class Parametros(Base):
    __tablename__ = "parametros"
    
    id_parametro = Column(Integer, primary_key=True, autoincrement=True)
    nombre_parametro = Column(String, nullable=False)
    valor_parametro = Column(String, nullable=False)
    fch_registro = Column(String, default='CURRENT_DATE')  # Cambia a DATE si es necesario

class Factura(Base):
    __tablename__ = "factura"
    
    id_factura = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String, nullable=False)
    fch_factura = Column(String, nullable=False)  # Cambia a DATE si es necesario
    total_pago = Column(NUMERIC, nullable=False)