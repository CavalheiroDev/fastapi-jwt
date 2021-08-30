from fastapi import APIRouter, status, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from app.api.schemas.user import UserLoginSchema
from app.database.events import SessionLocal
from app.database.repository import UserRepository
from app.middlewares.hashed_password import verify_password

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


router = APIRouter()


@router.post('/', status_code=status.HTTP_200_OK)
def login(payload: UserLoginSchema, typ: str = Header('JWT'), alg: str = Header('HS256') ,db: Session = Depends(get_db)):

    headers = {'typ': typ, 'alg': alg}
    

    user = UserRepository.get_user_by_email(db=db, payload=payload)
    
    if verify_password(payload.password, user.password):
        return {
            'message': 'Login feito com sucesso',
            'user': user.fullname,
            'email': user.email,
            'token': ''
        }
    return HTTPException(404, "Usuario não encontrado")
