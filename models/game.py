from config.database import Base
from sqlalchemy import Column, Integer, String, Float



class Game(Base):
    __tablename__ = "games"  # nombre que va a tener la tabla

    id = Column(Integer, primary_key=True,autoincrement=True)
    titulo = Column(String)
    sinopsis = Column(String)
    anio = Column(Integer)
    metaScore = Column(Float)
    categoria = Column(String)
