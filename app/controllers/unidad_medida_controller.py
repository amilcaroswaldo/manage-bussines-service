from fastapi import APIRouter
from ..services import unidad_medida_service
from ..models import services_models
from ..models.common_responses import GenericResponse, ObjectResponse, ListResponse
import pdb 
router = APIRouter(
    prefix="/UnidadMedida",
    tags=["UnidadMedida"],
    responses={404: {"description": "Not found"}},
)

@router.get("/allUnidadMedida", response_model= ListResponse[services_models.UnidadMedidaResponse] | GenericResponse)
async def getAllUnidadMedida() -> ListResponse[services_models.ServicioResponse] | GenericResponse:
    try:
        return await unidad_medida_service.getAllUnidadMedida()
    except Exception as e:
        return GenericResponse(code=500, message=str(e))

@router.post("/InsertUnidadMedida", status_code=201)
async def insertUnidadMedida(requestController: services_models.UnidadMedidaBase) -> ObjectResponse[services_models.UnidadMedidaResponse | None] | GenericResponse:
    try:
        return await unidad_medida_service.insertUnidadMedida(req=requestController)
    except ValueError as e:
        return GenericResponse(code=400, message=str(e))
    except Exception as e:
        return GenericResponse(code=500, message=str(e))

@router.put("/updateUnidadMedida")
async def updateUnidadMedida(request: services_models.UnidadMedidaRequestUpdate) -> GenericResponse:
    try:
        updated_service = await unidad_medida_service.actualizarServicio(request)
        if updated_service is None:
            return GenericResponse(code=404, message="Servicio no encontrado")
        return updated_service
    except ValueError as e:
        return GenericResponse(code=400, message=str(e))
    except Exception as e:
        return GenericResponse(code=500, message=str(e))

@router.delete("/deleteUnidadMedida/{unidad_medida_id}")
async def deleteUnidadMedida(unidad_medida_id: int) -> GenericResponse:
    try:
        deleted_service = await unidad_medida_service.eliminarUnidaMedida(unidad_medida_id=unidad_medida_id)
        if deleted_service is None:
            return GenericResponse(code=404, message="Servicio no encontrado")
        return deleted_service
    except ValueError as e:
        return GenericResponse(code=400, message=str(e))
    except Exception as e:
        return GenericResponse(code=500, message=str(e))