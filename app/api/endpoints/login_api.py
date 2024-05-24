# login_api.py

# lib
from fastapi.routing import APIRouter
from fastapi.responses import Response, JSONResponse
import json

# pkg
from app.schema.login_schema import LoginSchema
from app.service.login_service import LOGIN_SERVICE




router = APIRouter()

@router.post("/login")
async def login( data:LoginSchema ):
    result = await LOGIN_SERVICE.check_id( data )

    if result == 1:  # id not found
        return JSONResponse(status_code=404, content={"msg": "id not found !"})

    elif result == 2:  # wrong pw, Unauthorized
        return JSONResponse(status_code=401, content={"msg": "wrong password !"})

    else:
        resp = JSONResponse(status_code=200, content={"msg": "Login successful!", "user": result["user"]})
        resp.set_cookie(
            key="access_token",
            value=result["access_token"],
            httponly=True,
            max_age=3600,
            path="/"
        )
        return resp


@router.post("/logout")
async def logout(  ):
    print("로그아웃 중...")
    resp = JSONResponse(content={"msg":"로그아웃 성공"})
    resp.delete_cookie(key="access_token")
    print("로그아웃 !")
    return resp

