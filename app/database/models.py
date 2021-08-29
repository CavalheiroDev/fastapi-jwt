from sqlalchemy import Column, Integer, Text, VARCHAR
from sqlalchemy_utils import PasswordType
from app.database.events import Base


class User(Base):

    __tablename__ = 'users'

    id = Column('id', Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    fullname = Column('nome', Text(125), nullable=False)
    email = Column('email', VARCHAR(125), nullable=False)
    password = Column('senha', PasswordType(
            schemes=[
                'pbkdf2_sha512',
                'md5_crypt'
            ],
            deprecated=['md5_crypt']), 
            nullable=False)

    def __init__(self, fullname, email, password):
        self.fullname = fullname
        self.email = email
        self.password = password