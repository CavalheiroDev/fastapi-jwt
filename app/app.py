from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import login, register
from app.database.events import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:8000'],
    allow_credentials=True,
    allow_methods=['POST', 'GET'],
    allow_headers=['*'],
)
app.include_router(login.router, prefix='/login', tags=['login'])
app.include_router(register.router, prefix="/register", tags=['register'])