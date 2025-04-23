from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

from app.dbfactory import db_startup
from app.routes.member import member_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    db_startup()  # 서버 시작 시 DB 초기화
    yield

app = FastAPI(lifespan=lifespan)  # ✅ lifespan 연동

# 세션 미들웨어
app.add_middleware(SessionMiddleware, secret_key='02232024duedate')

# 라우터 등록
app.include_router(member_router)

# 정적 파일 + 템플릿 설정
app.mount('/static', StaticFiles(directory='views/static'), name='static')
templates = Jinja2Templates(directory='views/templates')

# 루트 페이지
@app.get("/", response_class=HTMLResponse)
async def index(req: Request):
    return templates.TemplateResponse('index.html', {'request': req})

# 개발 실행
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)
