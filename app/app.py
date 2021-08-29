from fastapi import FastAPI
from app.api.routes import router as UserRouter

app = FastAPI()


app.add_api_route(UserRouter, prefix='/login', tags=['users'])