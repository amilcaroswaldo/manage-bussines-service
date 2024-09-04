from ..models import services_models
from ..models.common_responses import GenericResponse, ObjectResponse, ListResponse
import pdb 
from ..repositories import unidad_medida_repository

async def getAllUnidadMedida():
    try:
        getUnidadMedida = await unidad_medida_repository.obtener_unidad_medida()
        return ListResponse(
            code=200, message="Servicios obtenidos exitosamente", items=getUnidadMedida
        )
    except Exception as e:
        return GenericResponse(code=500, message=str(e))

async def insertUnidadMedida(req: services_models.UnidadMedidaBase):
    try:
        insertUnidadMedida = await unidad_medida_repository.insertar_unidad_medida(request=req)
        return ObjectResponse(
            code=201, message="Servicio creado exitosamente", item=insertUnidadMedida
        )
    except Exception as e:
        return GenericResponse(code=500, message=str(e))

async def actualizarUnidadMedida(requestService: services_models.UnidadMedidaRequestUpdate):
    try:
        actualUnidad = await unidad_medida_repository.actualizar_unidad_medida(
            data=requestService
        )
        if actualUnidad:
            return GenericResponse(
                code=200, message="Servicio actualizado exitosamente"
            )
        else:
            return GenericResponse(
                code=404, message=f"No se encontró el servicio con ID {requestService.id_servicio}"
            )
    except Exception as e:
        return GenericResponse(code=500, message=str(e))

async def eliminarUnidaMedida(unidad_medida_id: int):
    try:
        eliminarUnidad = await unidad_medida_repository.eliminar_unidad_medida(
            unidad_medida_id=unidad_medida_id
        )
        if eliminarUnidad:
            return GenericResponse(code=200, message="Servicio eliminado exitosamente")
        else:
            return GenericResponse(
                code=404, message=f"No se encontró el servicio con ID {unidad_medida_id}"
            )
    except Exception as e:
        return GenericResponse(code=500, message=str(e))