from fastapi.security import HTTPBearer# esto es para la autentificación
from fastapi import Request, HTTPException
from utils.jwt_manager import validate_token

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        # esta es la función necesaria para la validación de credenciales
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data["email"] != "alejandrofareloduarte@gmail.com" or data["password"] != "example":
            # raise sirve para tirar un error
            raise HTTPException(
                status_code=403, detail="Credenciales invalidas")