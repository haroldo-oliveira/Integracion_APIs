
import db
from models import Info_Ciudad
from sqlalchemy import and_, or_, text

# --- ORM SQL-ALCHEMY , GESTION DE DATABASE ---
def home():
    pass

if __name__ == '__main__':
    # Reseteamos la base de datos si existe
    db.Base.metadata.drop_all(bind=db.engine, checkfirst=True)
