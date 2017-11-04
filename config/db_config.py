"""
Created by anthony on 15.10.17
db_config
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DB_NAME = 'yatt_db'
DB_USER = 'yatt_user'
DB_PASSWORD = 'root'
DB_HOST = 'localhost'
DB_PORT = 5432


connection_string = f'postgres://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
db_engine = create_engine(connection_string)

Session = sessionmaker(bind=db_engine)
db_session = Session()

Base = declarative_base()


def init_db():
    print('Starting database')

    import models.user, models.project, models.task
    try:
        Base.metadata.create_all(bind=db_engine)

    except Exception as e:
        print('Could not start database. Cause: ' + str(e))

    else:
        print('Database has started')
