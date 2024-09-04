# from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.repositories.confurationdb.models import UnidadMedida
from .confurationdb.dbconfiguration import get_db
from ..models import services_models
import pdb

async def insertar_unidad_medida(request: services_models.UnidadMedidaBase):
    """
    The function `insertar_unidad_medida` inserts a new unit of measurement into the database
    asynchronously.
    
    :param request: The `insertar_unidad_medida` function is an asynchronous function that inserts a new
    unit of measurement into the database. It takes a request object of type
    `services_models.UnidadMedidaBase` as a parameter
    :type request: services_models.UnidadMedidaBase
    :return: The function `insertar_unidad_medida` is returning a list containing a single element,
    which is an instance of `services_models.UnidadMedidaResponse`. This instance is created by passing
    the attributes of the newly inserted `UnidadMedida` object (`nueva_unidad_medida`) as keyword
    arguments to the `services_models.UnidadMedidaResponse` constructor.
    """
    async for db in get_db():  # Usar async for para obtener la sesión
        nueva_unidad_medida = UnidadMedida(
            nombre_medida = request.nombre_medida,
            tipo_medida = request.tipo_medida
        )
        db.add(nueva_unidad_medida)
        await db.commit()
        await db.refresh(nueva_unidad_medida)
        return [services_models.UnidadMedidaResponse(**nueva_unidad_medida.__dict__)]

async def obtener_unidad_medida():
    """
    This Python async function retrieves a list of unit measurements from a database session.
    :return: A list of `services_models.UnidadMedidaResponse` objects created from the data retrieved
    from the database. Each object corresponds to an `UnidadMedida` entity fetched from the database and
    is initialized with the attributes of that entity.
    """
    async for db in get_db():  # Usar async for para obtener la sesión
        result = await db.execute(select(UnidadMedida))
        list_unidad_medida = result.scalars().all()
        return [
            services_models.UnidadMedidaResponse(**i_unidad_medida.__dict__)
            for i_unidad_medida in list_unidad_medida
        ]

async def actualizar_unidad_medida(data: services_models.UnidadMedidaRequestUpdate):
    """
    This Python async function updates a unit of measurement in a database based on the provided data.
    
    :param data: The function `actualizar_unidad_medida` is an asynchronous function that updates a unit
    of measurement in a database. It takes a parameter `data` of type
    `services_models.UnidadMedidaRequestUpdate`, which likely contains the information needed to update
    the unit of measurement
    :type data: services_models.UnidadMedidaRequestUpdate
    :return: an instance of `services_models.UnidadMedidaResponse` created from the SQLAlchemy object
    `unidad_medida`. If the `unidad_medida` object exists and is successfully updated in the database,
    the function returns the response object. If no `unidad_medida` object is found or updated, the
    function returns `None`.
    """
    async for db in get_db():  # Usar async for para obtener la sesión
        result = await db.execute(
            select(UnidadMedida).where(UnidadMedida.unidad_medida_id == data.unidad_medida_id)
        )
        unidad_medida = result.scalar_one_or_none()
        if data.nombre_medida is not None:
            unidad_medida.nombre_medida = data.nombre_medida
        if data.tipo_medida is not None:
            unidad_medida.unidad_medida_id = data.unidad_medida_id
        if unidad_medida:
            await db.commit()
            await db.refresh(unidad_medida)
            print(unidad_medida)
            return services_models.UnidadMedidaResponse.from_sqlalchemy(unidad_medida)
    return None

async def eliminar_unidad_medida(unidad_medida_id: int):
    """
    This async function deletes a unit of measurement by its service ID from the database.
    
    :param id_servicio: El parámetro `id_servicio` es el identificador único de un servicio en la base
    de datos. Se utiliza para buscar y eliminar la unidad de medida asociada a ese servicio
    :type id_servicio: int
    :return: The function `eliminar_unidad_medida` is returning an instance of
    `services_models.UnidadMedidaResponse` converted from the SQLAlchemy object representing the deleted
    unit of measurement (unidad_medida). If the unit of measurement is found and successfully deleted,
    the converted response object is returned. If the unit of measurement is not found, `None` is
    returned.
    """
    """Elimina un servicio por su id."""
    async for db in get_db():  # Usar async for para obtener la sesión
        result = await db.execute(
            select(UnidadMedida).where(UnidadMedida.unidad_medida_id == unidad_medida_id)
        )
        unidad_medida = result.scalar_one_or_none()
        if unidad_medida:
            await db.delete(unidad_medida)
            await db.commit()
            return services_models.UnidadMedidaResponse.from_sqlalchemy(unidad_medida)
        return None