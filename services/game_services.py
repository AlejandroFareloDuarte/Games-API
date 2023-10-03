from models.game import Game as GameModel
from schemas.games import Game

class GameService():
    def __init__(self, db) -> None:
        self.db = db
# QUERY se usa para consultar en la base de datos
    def get_games(self):
        all_games = self.db.query(GameModel).all()
        return all_games
    
    def get_game_by_id(self, id):
        game_by_id:int = self.db.query(GameModel).filter(GameModel.id == id).first()
        return game_by_id
    
    def get_game_by_title(self, titulo):
        game_by_title = self.db.query(GameModel).filter(GameModel.titulo == titulo).first()
        return game_by_title
    
    def get_game_by_category(self, categoria):
        game_by_category:str = self.db.query(GameModel).filter( GameModel.categoria == categoria).all()
        return game_by_category
    
    def get_games_by_year(self, año):
        games_by_year:int =  self.db.query(GameModel).filter(GameModel.anio == año).all()
        return games_by_year
    
    def create_game(self, game: Game):
        new_game = GameModel(**game.dict())
        self.db.add(new_game)
        self.db.commit()
        return 
    
    def update_game(self, id: int, data: Game):
        upadated_game = self.db.query(GameModel).filter(GameModel.id == id).first()
        upadated_game.titulo = data.titulo
        upadated_game.sinopsis = data.sinopsis
        upadated_game.anio = data.anio
        upadated_game.metaScore = data.metaScore
        upadated_game.categoria = data.categoria
        self.db.commit()
        return
    
    def delete_game(self, id: int):
        self.db.query(GameModel).filter(GameModel.id == id).delete()
        self.db.commit()
        return
