from fastapi import FastAPI
from routers import users, topics, genders

app = FastAPI()

app.include_router(users.router)
app.include_router(topics.router)
app.include_router(genders.router)