from fastapi import APIRouter
from fastapi.responses import JSONResponse
from schemas.user import User
from utils.jwt_manager import create_token


user_router = APIRouter()

# aqui se crea una sección para autentificar
@user_router.post("/login", tags=["auth"])
def login(user: User):  # aqui estamos dando como parametros user de clase User
    if user.email == "alejandrofareloduarte@gmail.com" and user.password == "example":
        # aqui se devuelven los datos del usuario como diccionario
        token: str = create_token(user.dict())
        return JSONResponse(status_code=202, content=token)
    return JSONResponse(status_code=401, content={"message": "autentificación no valida."})