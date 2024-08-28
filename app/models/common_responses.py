from pydantic import BaseModel
from typing import Any, List, Generic, TypeVar

# Definimos un tipo genérico para las respuestas de lista
T = TypeVar('T')

class GenericResponse(BaseModel):
    code: int
    message: str
    # class  config:
    #     orm_mode = True  # Permite que Pydantic lea los datos de los modelos de SQLAlchemy
    #     model_config = {'from_attributes': True}      

class ObjectResponse(BaseModel, Generic[T]):
    code: int
    message: str
    item: T  # El elemento que se devuelve como parte de la respuesta
    # class  config:
    #     orm_mode = True  # Permite que Pydantic lea los datos de los modelos de SQLAlchemy
    #     model_config = {'from_attributes': True}       

class ListResponse(BaseModel, Generic[T]):
    code: int
    message: str
    items: List[T]  # Lista de elementos que se devuelven como parte de la respuesta
    # class  config:
    #     orm_mode = True  # Permite que Pydantic lea los datos de los modelos de SQLAlchemy
    #     model_config = {'from_attributes': True}    