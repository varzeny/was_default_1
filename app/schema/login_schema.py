from pydantic import BaseModel


class LoginSchema(BaseModel):
    id : str
    pw : str