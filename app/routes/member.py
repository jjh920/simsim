from fastapi import APIRouter, Form, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.schemas.member import NewMember
from app.services.member import MemberService
from app.dbfactory import get_db  # ✅ 이걸 써야 합니다!

member_router = APIRouter()

templates = Jinja2Templates(directory='views/templates')
member_router.mount('/static', StaticFiles(directory='views/static'), name='static')

@member_router.get('/login', response_class=HTMLResponse)
def login(req: Request):
    return templates.TemplateResponse('login/login.html', {'request': req})

@member_router.get('/join', response_class=HTMLResponse)
def join(req: Request):
    return templates.TemplateResponse('join/join.html', {'request': req})

@member_router.post('/join')
def joincheck(mdto: NewMember):
    result = MemberService.insert_member(mdto)
    return result.rowcount

@member_router.get("/check-id")
def check_id(userid: str, db: Session = Depends(get_db)):
    exists = MemberService.check_userid(userid, db)
    return {"exists": exists}

@member_router.get("/check-phone")
def check_phone(phone: str, db: Session = Depends(get_db)):
    exists = MemberService.check_phone(phone, db)
    return {"exists": exists}

@member_router.get('/joinok', response_class=HTMLResponse)
def joinok(req: Request):
    return templates.TemplateResponse('join/joinok.html', {'request': req})
