# login_service.py

# lib
from fastapi import Request

# pkg
from app.schema.login_schema import LoginSchema
from app.database.model.user_model import User
from app.database.dao.user_dao import USER_DAO
from app.core.security.auth import AUTH


class LoginService:
    def __init__(self) -> None:
        pass


    async def check_id( self, data:LoginSchema ):
        user = await USER_DAO.user_read( data.id )
        if user:
            if user.pw == data.pw:
                access_token = await AUTH.create_access_token( data.id )
                result = {
                    "user":{
                        "id":user.id
                    },
                    "access_token":access_token
                }
                print("계정있음 !")
                return result
            else:   # pw 틀림
                return 2
        else:   # id 없음
            return 1
        

    async def check_login( self, req:Request ):
        token = req.cookies.get( "access_token" )
        if token:
            result = await AUTH.verify_access_token( token )
            if result == 1:
                return False
            elif result == 2:
                return False
            else:
                return result




LOGIN_SERVICE = LoginService()