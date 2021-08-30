from fastapi import APIRouter, status, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from app.api.schemas.user import UserLoginSchema
from app.api.schemas.jwt import LoginJWTSchema
from app.database.events import SessionLocal
from app.database.repository import UserRepository
from app.middlewares.hashed_password import verify_password
from app.middlewares.jwt import generate_jwt_token, validate_jwt_token

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


router = APIRouter()


@router.get('/', response_model=LoginJWTSchema, status_code=status.HTTP_200_OK)
def read_logins(token_jwt: str = Header(None), db: Session = Depends(get_db)):
    
    if validate_jwt_token(token_jwt):
        users = UserRepository.get_all_users(db=db)
        return {
            'message': 'Autenticado com sucesso',
            'users': users
        }
    raise HTTPException(401, 'Token de acesso invalido')

@router.post('/', status_code=status.HTTP_200_OK)
def login(payload: UserLoginSchema, typ: str = Header('JWT'), alg: str = Header('HS256') ,db: Session = Depends(get_db)):

    headers = {'typ': typ, 'alg': alg}

    token_jwt = generate_jwt_token(headers, payload)

    user = UserRepository.get_user_by_email(db=db, payload=payload)
    
    if verify_password(payload.password, user.password):
        return {
            'message': 'Login feito com sucesso',
            'token': token_jwt
        }
    return HTTPException(404, "Usuario não encontrado")
