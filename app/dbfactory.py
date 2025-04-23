from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.settings import config
from app.models import member

# DB 엔진 생성
engine = create_engine(config.db_conn, echo=True)

# 세션 팩토리 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 테이블 생성용 함수
def db_startup():
    member.Base.metadata.create_all(engine)

# 의존성 주입용 DB 세션 함수
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
