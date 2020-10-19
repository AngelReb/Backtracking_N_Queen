#http://zetcode.com/db/sqlalchemy/
#https://docs.sqlalchemy.org/en/13/orm/tutorial.html
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

Session = sessionmaker()
DATABASE_URI ='postgresql://angel:postgres@db/coding_challenge'
engine = create_engine(DATABASE_URI, echo=True)
#db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Session.configure(bind=engine)

session = Session(autocommit=False )

Base = declarative_base()



