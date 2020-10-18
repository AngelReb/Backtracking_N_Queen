#http://zetcode.com/db/sqlalchemy/
#https://docs.sqlalchemy.org/en/13/orm/tutorial.html
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine('postgresql://angel:postgres@0.0.0.0:5432/coding_challenge', echo=True)
#db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()

Session = sessionmaker()
Session.configure(bind=engine)

session = Session()


def init_db():
	Base.metadata.create_all(bind=engine)

