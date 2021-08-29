from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    fullname: str = Field(...)
    email: str = Field(...)
    password: str = Field(..., min_length=6)

    class Config:
        orm_mode = True
        schema_extra = {
            'fullname': 'Gabriel Cavalheiro Barreto',
            'email': 'gabriel.cavalheiro-barreto@teste.com.br',
            'password': 'senhasupersecreta1234'
        }


class UserLoginSchema(BaseModel):
    email: str = Field(...)
    password: str = Field(..., min_length=6)

    class Config:
        orm_mode = True
        schema_extra = {
            'email': 'gabriel.cavalheiro-barreto@teste.com.br',
            'password': 'senhasupersecreta1234' 
        }