from fastapi import APIRouter, Path, Depends,Query
from fastapi.responses import JSONResponse
from schemas.games import Game 
from config.database import Session
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.game_services import GameService
from typing import List
from models.game import Game as GameModel



game_router = APIRouter()

# los codigos de estado son las respuestas predeterminadas de las funciones
# la parte de dependencies es para que esa opción solo sea pueda usar si se cumple la autentificación
# Define una dependencia para la autenticación JWT
def get_current_user(token: str = Depends(JWTBearer())):
    return token

game_router = APIRouter(dependencies=[Depends(get_current_user)])#,dependencies=[Depends(JWTBearer())], dependencies=[Depends(get_current_user)]

@game_router.get("/juegos", tags=["Juegos"])
def get_games() ->List[Game]:
    db = Session()  # siempre que queramos consultar de manipular la base de datos se necesita session
    result = GameService(db).get_games()
    db.close()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@game_router.get("/juegos/{id}", tags=["Juegos"])
# con path estamos validando los datos dentro de las funciones
def get_game_by_id(id: int = Path(ge=1, le=2000)) -> Game:
    db = Session()
    result_by_id: int = GameService(db).get_game_by_id(id)
    db.close()
    if result_by_id:
        return JSONResponse(status_code=200, content=jsonable_encoder(result_by_id))
    return JSONResponse(status_code=404, content={"message": "Juego no encontrado."})


@game_router.get("/juegos/titulo/{Titulo}", tags=["Juegos"])
def get_game_by_title(titulo: str = Query(min_length=1)) ->Game:
    db = Session()
    result_by_title: str = GameService(db).get_game_by_title(titulo)
    db.close()
    if result_by_title:
        return JSONResponse(status_code=200, content=jsonable_encoder(result_by_title))
    return JSONResponse(status_code=404, content={"message": "Juego no encontrado."})


@game_router.get("/juegos/categoria/{Categoria}", tags=["Juegos"])
def get_game_by_category(categoria: str = Query(min_length=1)) ->List[Game]:
    db = Session()
    games_filtered_by_category: str = GameService(db).get_game_by_category(categoria)
    db.close()
    if games_filtered_by_category:
        return JSONResponse(status_code=200, content=jsonable_encoder(games_filtered_by_category))
    return JSONResponse(status_code=404, content={"message": "Juegos no encontrados con esta categoria."})


@game_router.get("/juegos/año/{año}", tags=["Juegos"])
def get_game_by_year(anio: int = Query(ge=1, le=2024)):
    db = Session()
    games_filtered_by_year: int = GameService(db).get_games_by_year(anio)
    db.close()
    if games_filtered_by_year:
        return JSONResponse(status_code=200, content=jsonable_encoder(games_filtered_by_year))
    return JSONResponse(status_code=404, content={"message": "Juegos no encontrados para este año."})


# Post permite que el usuario ingrese datos
@game_router.post("/Juegos", tags=["Juegos"])
# estamos diciendo que queremos un objeto(game) de tipo Game(esquema)
def create_game(game: Game):
    db = Session()
    GameService(db).create_game(game)
    db.close()
    return JSONResponse(status_code=201, content={"message":"Juego creado."})


@game_router.put("/Juegos/{id}", tags=["Juegos"])  # put sirve para modificar
# estamos diciendo que queremos un objeto(game) de tipo Game(esquema)
def modify_game(game: Game, id: int = Path(ge=1, le=2000))->Game:
    db = Session()
    modified_game = GameService(db).get_game_by_id(id)
    db.close()
    if not modified_game:
        return JSONResponse(status_code=404, content={"message": "Id no encontrado para modificar."})
    GameService(db).update_game(id, game)
    return JSONResponse(status_code=202, content={"message": "Juego modificado."})


@game_router.delete("/Juegos/{id}", tags=["Juegos"])  # Eliminar un elemento
def delete_game(id: int) -> dict:
    db = Session()
    deleted_game: GameModel = db.query(GameModel).filter(GameModel.id == id).first()
    db.close()
    if not deleted_game:
        return JSONResponse(status_code=404, content={"message": "Id no encontrado para eliminar."})
    GameService(db).delete_game(id)
    return JSONResponse(status_code=202, content={"message": "Juego eliminado."})