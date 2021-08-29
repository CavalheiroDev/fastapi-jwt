from pydantic import BaseModel, Field, EmailStr


class UserSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(..., min_length=6)

    class Config:
        schema_extra = {
            'fullname': 'Gabriel Cavalheiro Barreto',
            'email': 'gabriel.cavalheiro-barreto@teste.com.br',
            'password': 'senhasupersecreta1234'
        }


class UserLoginSchema(BaseModel):
    email: str = EmailStr(...)
    password: str = Field(..., min_length=6)

    class Config:
        schema_extra = {
            'email': 'gabriel.cavalheiro-barreto@teste.com.br',
            'password': 'senhasupersecreta1234' 
        }