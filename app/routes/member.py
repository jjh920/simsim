from fastapi import APIRouter, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from starlette import status
from starlette.responses import RedirectResponse

from app.schemas.member import NewMember
from app.services.member import MemberService


from fastapi import HTTPException

member_router = APIRouter()

templates = Jinja2Templates(directory='views/templates')

member_router.mount('/static', StaticFiles(directory='views/static'), name='static')

@member_router.get('/login', response_class=HTMLResponse)
def join(req: Request):
    return templates.TemplateResponse('login/login.html', {'request': req})

@member_router.get('/login2', response_class=HTMLResponse)
def join2(req: Request):
    return templates.TemplateResponse('login/login.html', {'request': req})