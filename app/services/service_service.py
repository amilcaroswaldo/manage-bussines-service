from ..repositories import service_repository
from ..models import services_models
from ..models.common_responses import GenericResponse, ObjectResponse, ListResponse
import pdb 

async def getAllServices():
    try:
        getServices = await service_repository.obtener_servicios()
        return ListResponse(
            code=200, message="Servicios obtenidos exitosamente", items=getServices
        )
    except Exception as e:
        return GenericResponse(code=500, message=str(e))


async def insertServices(req: services_models.ServicioCreateRequest):
    try:
        insertService = await service_repository.insertar_servicio(request=req)
        return ObjectResponse(
            code=201, message="Servicio creado exitosamente", item=insertService
        )
    except Exception as e:
        return GenericResponse(code=500, message=str(e))


async def obtenerServicioById(idServicio: int):
    try:
        getServiceId = await service_repository.obtener_servicio_por_id(
            id_servicio=idServicio
        )
        if getServiceId:
            return getServiceId
        else:
            return ObjectResponse(
                code=404,
                message=f"No se encontró el servicio con ID {idServicio}",
                item=None,
            )
    except Exception as e:
        return GenericResponse(code=500, message=str(e))


async def obtenerServicioByDescripcion(descripcionServicio: str):
    try:
        getService = await service_repository.obtener_servicio_por_descripcion(
            descripcion_servicio=descripcionServicio
        )
        if getService:
            return ObjectResponse(
                code=200, message="Servicio obtenido exitosamente", item=getService
            )
        else:
            return ObjectResponse(
                code=404,
                message=f"No se encontró el servicio con descripción '{descripcionServicio}'",
                item=None,
            )
    except Exception as e:
        return GenericResponse(code=500, message=str(e))


async def actualizarServicio(requestService: services_models.ServicioUpdateRequest):
    try:
        actualizarServicio = await service_repository.actualizar_servicio(
            data=requestService
        )
        if actualizarServicio:
            return GenericResponse(
                code=200, message="Servicio actualizado exitosamente"
            )
        else:
            return GenericResponse(
                code=404, message=f"No se encontró el servicio con ID {requestService.id_servicio}"
            )
    except Exception as e:
        return GenericResponse(code=500, message=str(e))


async def eliminarServicio(idServicio: int):
    try:
        eliminarServicio = await service_repository.eliminar_servicio(
            id_servicio=idServicio
        )
        if eliminarServicio:
            return GenericResponse(code=200, message="Servicio eliminado exitosamente")
        else:
            return GenericResponse(
                code=404, message=f"No se encontró el servicio con ID {idServicio}"
            )
    except Exception as e:
        return GenericResponse(code=500, message=str(e))
