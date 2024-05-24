# navigation_api.py

# lib
from fastapi.routing import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi import Depends, Query
from fastapi.responses import JSONResponse

# pkg
from app.core.security.auth import AUTH
from app.service.login_service import LOGIN_SERVICE

# init
router = APIRouter()
templates = Jinja2Templates(directory="app/templates")



@router.get("/")
async def get_index(request:Request, login=Depends( LOGIN_SERVICE.check_login )):
    return templates.TemplateResponse("index.html", {"request": request, "login": login})


@router.get("/get_html")
async def get_html( req:Request, target:str=Query(...), login=Depends( LOGIN_SERVICE.check_login ) ):
    if login:
        return templates.TemplateResponse( f"{target}.html",{"request":req} )
    else:
        return JSONResponse( status_code=401, content={"msg":"로그인 하시오 !"} )

# @router.get("/dashboard")
# async def get_dashboard( req:Request, login=Depends( LOGIN_SERVICE.check_login ) ):
#     print("대쉬보드 api 발동")

#     if login:
#         return templates.TemplateResponse("dashboard.html",{"request":req})
#     else:
#         return JSONResponse( status_code=401, content={"msg":"로그인 하시오 !"} )

    
