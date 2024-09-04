from fastapi import FastAPI,Request
from app.controllers.services_controllers import router as servicesControllers
from app.controllers.unidad_medida_controller import router as unidadControllers
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
app = FastAPI()

app.include_router(servicesControllers)
app.include_router(unidadControllers)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"code": 422, "message": "Validation Error", "errors": exc.errors()},
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)