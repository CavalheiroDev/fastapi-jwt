from sqlalchemy.orm import Session
from app.database.models import User
from app.api.schemas import UserSchema, UserLoginSchema


class UserRepository():
    async def create_user(self, db: Session, payload: UserSchema):
        user = User(payload.fullname, payload.email, payload.password)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    