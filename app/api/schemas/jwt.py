from typing import List
from pydantic import BaseModel
from app.api.schemas.user import UserLoginSchema


class LoginJWTSchema(BaseModel):

    message: str
    users: List[UserLoginSchema] = []

    class Config:
        orm_mode = True