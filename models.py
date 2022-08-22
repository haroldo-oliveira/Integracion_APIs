import db
from sqlalchemy import Column, Integer, String, Boolean

# --- MODELS, GESTIONA LAS CLASES/TABLAS DB (POO) ---
class Info_Ciudad(db.Base):
    __tablename__ = "info_ciudad"
    id = Column(Integer, primary_key=True)

    ciudad = Column(String(50), nullable=False)

    estado_cielo = Column(String(100))

    temperatura = Column(Integer)

    hecha = Column(Boolean)

    def __init__(self, ciudad, estado_cielo, temperatura, hecha):
        self.ciudad = ciudad
        self.estado_cielo = estado_cielo
        self.temperatura = temperatura
        self.hecha = hecha

    def __str__(self):
        return """
        id: {}\n
        Info: {} \n
        Estado Cielo: {}\n
        Temperatura: {}\n
        Hecha: ({})""".format(self.id, self.ciudad, self.estado_cielo,
                              self.temperatura, self.hecha)
