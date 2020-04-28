import sqlalchemy
from sqlalchemy import orm
from db import db_folder
from data.sqlalchemybase import SqlAlchemyBase

__engine = None
__factory = None

def global_init(db_name: str):
    global __engine, __factory

    if __factory:
        return
    conn_str = 'sqlite:///' + db_folder.get_full_path(db_name)
    __engine = sqlalchemy.create_engine(conn_str, echo=False)
    __factory = sqlalchemy.orm.sessionmaker(bind=__engine)

def create_tables():
    if not __engine:
        raise Exception('Global init not called')
    import data.all_models
    SqlAlchemyBase.metadata.create_all(__engine)



