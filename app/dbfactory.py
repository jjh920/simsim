from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.settings import config

from app.models import member


engine = create_engine(config.db_conn, echo=True)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def db_startup():
    member.Base.metadata.create_all(engine)