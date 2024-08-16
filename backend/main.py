from fastapi import FastApi
from database import engine
import models
from router import router

models.Base.metadata.create_all(bind=engine)

app = FastApi()
app.include_router(router)