# auth.py

# lib
from jose import jwt, JWTError, ExpiredSignatureError


# pkg



class Auth:
    
    def __init__(self) -> None:
        self.secret_key = None
        self.algorithm = None
        self.token_expire = None


    def setting( self, config_data ):
        self.secret_key = config_data[ "secret_key" ]
        self.token_expire = config_data[ "token_expire" ]
        self.algorithm = config_data[ "algorithm" ]


    async def create_access_token(self, sub:str) -> str:
        payload = {
            "sub":sub
        }

        return jwt.encode( payload, self.secret_key, algorithm=self.algorithm )
    

    async def verify_access_token(self, token:str):
        print("토큰 확인 중...")

        try:
            payload = jwt.decode( token, self.secret_key, algorithms=self.algorithm )
            print("정상 토큰 !")
            print("payload : ",payload)
            return payload
        except ExpiredSignatureError:   # 기간 만료
            print( "기간 만료 !" )
            return 1
        except JWTError:    # 순수한 에러
            print( "순수한 토큰 에러 !" )
            return 2

    




AUTH = Auth()