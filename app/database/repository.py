from sqlalchemy.orm import Session
from app.database.models import User
from app.api.schemas.user import UserSchema, UserLoginSchema


class UserRepository():
    def create_user(db: Session, payload: UserSchema):
        user = User(payload.fullname, payload.email, payload.password)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    
    def get_user_by_email(db: Session, payload: UserLoginSchema):
        user = db.query(User).filter(User.email == payload.email).first()
        if user != []:
            return user
        return []
        
    def get_all_users(db: Session):
        users = db.query(User).order_by('id').all()
        if users != []:
            return users
        return []