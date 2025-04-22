from pydantic import BaseModel
from datetime import datetime





class Member(BaseModel):
    mno: int
    userid: str
    pwd: str
    name: str
    phone: str
    email: str
    regdate: datetime

    class Config:
        from_attributes = True


class NewMember(BaseModel):
    userid: str
    pwd: str
    name: str
    phone: str
    email: str


