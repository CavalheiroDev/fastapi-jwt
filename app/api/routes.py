from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from app.api.schemas import UserSchema, UserLoginSchema
from app.database.events import SessionLocal
from app.database.repository import UserRepository

def get_db():
    try:
        db = SessionLocal()
    finally:
        db.close()


router = APIRouter()


@router.get('/', status_code=status.HTTP_200_OK)
def login(user: UserLoginSchema):
    pass


@router.post('/', status_code=status.HTTP_201_CREATED)
def register(payload: UserSchema, db: Session = Depends(get_db)):
    user = UserRepository.create_user(db=db, payload=payload)
    return {
        'message': 'Usuario criado com sucesso',
        'User': user
    }