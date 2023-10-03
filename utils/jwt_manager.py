#esto es para la autentificación 
from jwt import encode, decode

def create_token(data: dict) ->str:
    token: str = encode(payload=data, key="password", algorithm="HS256")#payload contenido covertido a token, key es la llave para decifrar el token, algorithm es el algoritmo con el q se genera el token
    return token

def validate_token(token: str) -> dict: 
    data: dict = decode(token, key="password", algorithms=["HS256"])#esto es para decodificaar el codigo
    return data 