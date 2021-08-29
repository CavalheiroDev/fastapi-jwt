from fastapi import FastAPI
from app.api.routes import router as UserRouter
from app.database.events import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(UserRouter, prefix='/login', tags=['login'])