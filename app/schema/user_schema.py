from pydantic import BaseModel











class UserCreate(BaseModel):
    id: str
    pw: str

class UserRead(BaseModel):
    id: str
    pw: str

    class Config:
        orm_mode = True