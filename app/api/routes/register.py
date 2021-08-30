from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from app.api.schemas.user import UserSchema
from app.database.events import SessionLocal
from app.database.repository import UserRepository
from app.middlewares.hashed_password import generate_hashed_password

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED)
def register(payload: UserSchema, db: Session = Depends(get_db)):
    new_user = payload
    new_user.password = generate_hashed_password(payload.password)
    user = UserRepository.create_user(db=db, payload=new_user)
    return {
        'message': 'Usuario criado com sucesso',
        'User': user
    }