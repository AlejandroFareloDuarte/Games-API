from pydantic import BaseModel, Field #Para la creación de esquemas se puede usar Pydantic, Field se usa para validar y limitar los datos.
from typing import Optional


class Game(BaseModel): #Para crear el modelo la clase tiene que heredar de basemodel
    id: Optional[int] = None
    titulo: str = Field(min_length=1, max_length=100)
    sinopsis: str = Field(max_length=1000, min_length=10)
    anio: int = Field(le=2023)#Le = less or equal
    metaScore: float = Field(le=10, ge=0)#ge = greater than or equal 
    categoria: str = Field(min_length=3, max_length=100)

    class Config: #Esto es una base por si el usuario no rellena nada en el campo 
        schema_extra = {
            "example":
            {
                "Titulo": "Ejemplo",
                "Sinopsis": "......",
                "Año": 1900,
                "MetaScore": 0.0,
                "Categoria": "......"
            }
        }