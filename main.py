import db
from models import Info_Ciudad

if __name__ == '__main__':
    # Reseteamos la base de datos si existe
    db.Base.metadata.drop_all(bind=db.engine, checkfirst=True)

    #  En la siguiente linea estamos indicando a SQLAlchemy que cree, si no existen, las tablas de
    #  todos los modelos que encuentre en la aplicación. Sin embargo, para que esto ocurra es necesario
    #  que cualquier modelo se haya importado previamente antes de llamar a la función create_all().

    db.Base.metadata.create_all(db.engine)  # inicia la creacion de todos los modelos via engine en db.py
