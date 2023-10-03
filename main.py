# path y query son para validar datos, path numericos, query strs
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse# JSON es para respuestas 
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler 
from routers.game_router import game_router
from routers.user_router import user_router



app = FastAPI()
app.title = "GamesHub"
app.version = "1.5.0"
app.add_middleware(ErrorHandler)#Esto es para manejar errores

@app.get("/", tags=["Home"])
def message():
    return HTMLResponse("Bienvenido a GamesHub")

app.include_router(user_router)
app.include_router(game_router)#Aqui nos traemos todo del router para main


Base.metadata.create_all(bind=engine)






