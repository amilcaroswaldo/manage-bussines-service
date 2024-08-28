from fastapi import APIRouter
from ..services import service_service
from ..models import services_models
from ..models.common_responses import GenericResponse, ObjectResponse, ListResponse

router = APIRouter(
    prefix="/servicios",
    tags=["Servicios"],
    responses={404: {"description": "Not found"}},
)

@router.get("/allServices", response_model= ListResponse[services_models.ServicioResponse] | GenericResponse)
async def getAllService() -> ListResponse[services_models.ServicioResponse] | GenericResponse:
    try:
        return await service_service.getAllServices()
    except Exception as e:
        return GenericResponse(code=500, message=str(e))

@router.post("/InsertService", status_code=201)
async def insertService(requestController: services_models.ServicioCreateRequest) -> ObjectResponse[services_models.ServicioResponse | None] | GenericResponse:
    try:
        return await service_service.insertServices(req=requestController)
    except ValueError as e:
        return GenericResponse(code=400, message=str(e))
    except Exception as e:
        return GenericResponse(code=500, message=str(e))

@router.get("/getServiceByID/{idServicioReq}")
async def getServiceByID(idServicioReq: int) -> GenericResponse | ObjectResponse[services_models.ServicioResponse]:
    try:
        service = await service_service.obtenerServicioById(idServicio=idServicioReq)
        if service is None:
            return GenericResponse(code=404, message="Servicio no encontrado")
        return ObjectResponse(code=200, message="Servicio obtenido exitosamente", item=service)
        # return service
    except ValueError as e:
        return GenericResponse(code=400, message=str(e))
    except Exception as e:
        return GenericResponse(code=500, message=str(e))

@router.get("/getServiceByDescripcion")
async def getServiceByDescripcion(descripcionServicio: str) -> GenericResponse | ObjectResponse[services_models.ServicioResponse] :
    try:
        service = await service_service.obtenerServicioByDescripcion(descripcionServicio=descripcionServicio)
        print(service)
        if service is None:
            return GenericResponse(code=404, message="Servicio no encontrado")
        return service
    except ValueError as e:
        return GenericResponse(code=400, message=str(e))
    except Exception as e:
        return GenericResponse(code=500, message=str(e))

@router.put("/updateService/{idServicio}")
async def updateService(idServicio: int, requestService: services_models.ServicioCreateRequest) -> GenericResponse:
    try:
        updated_service = await service_service.actualizarServicio(idServicio=idServicio, requestService=requestService)
        if updated_service is None:
            return GenericResponse(code=404, message="Servicio no encontrado")
        return GenericResponse(code=200, message="Servicio actualizado exitosamente")
    except ValueError as e:
        return GenericResponse(code=400, message=str(e))
    except Exception as e:
        return GenericResponse(code=500, message=str(e))

@router.delete("/deleteService/{idServicio}")
async def deleteService(idServicio: int) -> GenericResponse:
    try:
        deleted_service = await service_service.eliminarServicio(idServicio=idServicio)
        if deleted_service is None:
            return GenericResponse(code=404, message="Servicio no encontrado")
        return GenericResponse(code=200, message="Servicio eliminado exitosamente")
    except ValueError as e:
        return GenericResponse(code=400, message=str(e))
    except Exception as e:
        return GenericResponse(code=500, message=str(e))