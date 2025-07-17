from dotenv import load_dotenv
load_dotenv(override=True)

from fastapi import FastAPI
from app.api import router


app = FastAPI()

app.include_router(router)

