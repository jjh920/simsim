from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from app.models.base import Base


class Member(Base):
    __tablename__ = 'member'

    mno = Column(Integer, primary_key=True, autoincrement=True)     # 회원번호
    userid = Column(String(18), nullable=False, unique=True)        # 아이디
    pwd = Column(String(18), nullable=False)                        # 패스워드
    name = Column(String(20), nullable=False)                       # 이름
    phone = Column(String(11), nullable=False, unique=True)         # 전화번호
    email = Column(String(50), nullable=False, unique=True)         # 이메일
    regdate = Column(DateTime, default=datetime.now)                # 가입시간


class proposer(Base):
    __tablename__ = 'proposer'

    name = Column(String(20), primary_key=True)                      # 이름
    purpose = Column(String(20), nullable=False)                     # 방문목적
    vacation_start = Column(String(10), nullable=True)               # 휴가시작날짜
    vacation_end = Column(String(10), nullable=True)                 # 휴가마감날짜
    vno = Column(String(3), nullable=True)                           # 휴가일수
    vacation_date = Column(DateTime, default=datetime.now(), nullable=True) # 신청일