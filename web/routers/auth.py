from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from utils import get_templates

router = APIRouter(prefix='/auth', tags=['auth'])

templates = get_templates()


@router.get('/login', response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse(request, 'login.html', {'message': 'login'})


@router.get('/register', response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse(request, 'register.html', {'message': 'register'})


@router.get('/password_recovery', response_class=HTMLResponse)
async def greate_user(request: Request):
    return templates.TemplateResponse(request, 'password_recovery.html', {'message': 'password_recovery'})
