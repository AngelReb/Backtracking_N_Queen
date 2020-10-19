"""
    Documentacion oficial de SQLAlchemy y link oficial de ejemplos
    #https://docs.sqlalchemy.org/en/13/orm/tutorial.html
    #http://zetcode.com/db/sqlalchemy/

"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

Session = sessionmaker()
DATABASE_URI ='postgresql://angel:postgres@db/coding_challenge'
engine = create_engine(DATABASE_URI, echo=False)
#db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Session.configure(bind=engine)

session = Session(autocommit=False)

Base = declarative_base()



