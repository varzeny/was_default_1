# lib
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager

# pkg
from app.core.config import CONFIG
from app.core.security.auth import AUTH
from app.database.session import DB_SS
from app.api.api import ROUTERS


# uvicorn app.main:app --host 192.168.0.12 --port 9000 --reload


# 생성,소멸자
@asynccontextmanager
async def app_init(app:FastAPI):
    print( "앱이 시작됨 !" )

    # DB세팅
    DB_SS.setting( CONFIG[ "db" ] )
    await DB_SS.connect()

    # 인증 세팅
    AUTH.setting( CONFIG[ "security" ] )


    yield

    # DB 연결 해제
    await DB_SS.disconnect()

    print( "앱이 종료됨 !" )



# script #################################################################
app = FastAPI(
    lifespan=app_init
)


# 정적파일
app.mount(
    "/static", # 요청 URL
    StaticFiles(directory="app/static"), # 앱 내부 경로
    name="static"  # 뭐라고 부를지
)


# 라우터 추가
app.include_router( ROUTERS )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="192.168.0.12", port=9000, reload=True)