from pydantic import BaseModel

class User(BaseModel): #se crea la clase usuario
    email: str
    password: str   