from pydantic import BaseModel
from typing import Optional, List

# UnidadMedida Models
class UnidadMedidaBase(BaseModel):
    nombre_medida: str
    tipo_medida: str

    class Config:
        orm_mode = True

class UnidadMedidaCreate(UnidadMedidaBase):
    pass

class UnidadMedidaResponse(UnidadMedidaBase):
    unidad_medida_id: int

# CategoriaProducto Models
class CategoriaProductoBase(BaseModel):
    descripcion: str

    class Config:
        orm_mode = True

class CategoriaProductoCreate(CategoriaProductoBase):
    pass

class CategoriaProductoResponse(CategoriaProductoBase):
    categoria_prod_id: int

# Servicios Models
class ServicioBase(BaseModel):
    descripcion: str
    unidad_medida_id: int
    cantidad: int
    precio: float

    class Config:
        orm_mode = True

class ServicioCreateRequest(ServicioBase):
    pass

class ServicioResponse(ServicioBase):
    id_servicio: int

# Inventarios Models
class InventarioBase(BaseModel):
    nombre_producto: str
    cantidad_prod: float
    fch_ingreso: str
    fecha_vencimiento_prod: Optional[str]
    costo: float
    comentario: Optional[str]
    categoria_prod_id: int

    class Config:
        orm_mode = True

class InventarioCreate(InventarioBase):
    pass

class InventarioResponse(InventarioBase):
    id_inventario: int

# Parametros Models
class ParametroBase(BaseModel):
    nombre_parametro: str
    valor_parametro: str
    fch_registro: Optional[str] = 'CURRENT_DATE'

    class Config:
        orm_mode = True

class ParametroCreate(ParametroBase):
    pass

class ParametroResponse(ParametroBase):
    id_parametro: int

# Factura Models
class FacturaBase(BaseModel):
    descripcion: str
    fch_factura: str
    total_pago: float

    class Config:
        orm_mode = True

class FacturaCreate(FacturaBase):
    pass

class FacturaResponse(FacturaBase):
    id_factura: int
