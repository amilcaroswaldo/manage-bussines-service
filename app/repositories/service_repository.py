from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.repositories.confurationdb.models import Servicios
from .confurationdb.dbconfiguration import get_db
from ..models import services_models

async def insertar_servicio(request: services_models.ServicioCreateRequest):
    """Inserta un nuevo servicio en la base de datos."""
    async for db in get_db():  # Usar async for para obtener la sesión
        nuevo_servicio = Servicios(
            descripcion=request.descripcion,
            unidad_medida_id=request.unidad_medida_id,
            cantidad=request.cantidad,
            precio=request.precio
        )
        db.add(nuevo_servicio)
        await db.commit()
        await db.refresh(nuevo_servicio)
        return [services_models.ServicioResponse(**nuevo_servicio.__dict__)]

async def obtener_servicios():
    """Obtiene todos los servicios de la base de datos."""
    async for db in get_db():  # Usar async for para obtener la sesión
        result = await db.execute(select(Servicios))
        servicios = result.scalars().all()
        return [services_models.ServicioResponse(**servicio.__dict__) for servicio in servicios]

async def obtener_servicio_por_id(id_servicio: int):
    """Obtiene un servicio por su id."""
    async for db in get_db():  # Usar async for para obtener la sesión
        result = await db.execute(select(Servicios).where(Servicios.id_servicio == id_servicio))
        servicio = result.scalar_one_or_none()
        return services_models.ServicioResponse.from_sqlalchemy(servicio)

async def obtener_servicio_por_descripcion(descripcion_servicio: str):
    """Obtiene un servicio por su descripción."""
    async for db in get_db():  # Usar async for para obtener la sesión
        result = await db.execute(select(Servicios).where(Servicios.descripcion == descripcion_servicio))
        servicio = result.scalar_one_or_none()
        return services_models.ServicioResponse.from_sqlalchemy(servicio)

async def actualizar_servicio(id_servicio: int, request: services_models.ServicioCreateRequest):
    """Actualiza un servicio existente."""
    async for db in get_db():  # Usar async for para obtener la sesión
        servicio = await obtener_servicio_por_id(id_servicio)
        if servicio:
            servicio.descripcion = request.descripcion
            servicio.unidad_medida_id = request.unidad_medida_id
            servicio.cantidad = request.cantidad
            servicio.precio = request.precio
            await db.commit()
            await db.refresh(servicio)
            return services_models.ServicioResponse.from_orm(servicio)
        return None

async def eliminar_servicio(id_servicio: int):
    """Elimina un servicio por su id."""
    async for db in get_db():  # Usar async for para obtener la sesión
        servicio = await obtener_servicio_por_id(id_servicio)
        if servicio:
            await db.delete(servicio)
            await db.commit()
            return services_models.ServicioResponse.from_orm(servicio)
        return None
