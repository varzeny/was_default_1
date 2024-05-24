# lib
from datetime import datetime, timedelta
import json
import base64
import hmac
import hashlib

# pkg



class Auth:
    
    def __init__(self) -> None:
        self.secret_key = None
        self.algorithm = None
        self.token_expire = None


    async def setting( self, config_data ):
        self.secret_key = config_data[ "secret_key" ]
        self.token_expire = config_data[ "token_expire" ]
        self.algorithm = config_data[ "algorithm" ]

    
    def base64_url_encode(self, data: bytes) -> str:
        return ( base64.urlsafe_b64encode(data).rstrip(b'=') ).decode("utf-8")


    async def get_access_token(self, sub):
        header = {
            "alg":self.algorithm,
            "typ":"JWT"
        }
        header_json = json.dumps( header ).encode("utf-8")
        header_b64 = self.base64_url_encode( header_json )


        payload = {
            "sub":sub,
            "exp":int( ( datetime.utcnow() + timedelta( minutes=self.token_expire ) ).timestamp() )
        }
        payload_json = json.dumps( payload ).encode( "utf-8" )
        payload_b64 = self.base64_url_encode( payload_json )



        signature_input = f"{header_b64}.{payload_b64}".encode('utf-8')
        signature = hmac.new(self.secret_key.encode('utf-8'), signature_input, hashlib.sha256).digest()
        signature_b64 = self.base64_url_encode(signature)

        jwt_token = f"{header_b64}.{payload_b64}.{signature_b64}"
        return jwt_token
        


    


AUTH = Auth()