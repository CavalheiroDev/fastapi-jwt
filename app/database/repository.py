from sqlalchemy.orm import Session
from app.database.models import User
from app.api.schemas import UserSchema, UserLoginSchema


class UserRepository():
    def create_user(db: Session, payload: UserSchema):
        user = User(payload.fullname, payload.email, payload.password)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    
    def get_user_by_email(db: Session, payload: UserLoginSchema):
        return db.query(User).filter(User.email == payload.email).first()