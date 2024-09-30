from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import auth, chat, socket

app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), name='static')

app.include_router(auth.router)
app.include_router(chat.router)
app.include_router(socket.router)

