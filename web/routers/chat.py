from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from utils import get_templates

router = APIRouter(prefix='', tags=['chat'])

templates = get_templates()


@router.get('/', response_class=HTMLResponse)
async def chat(request: Request):
    return templates.TemplateResponse(request, 'chat.html', {'message': 'chat'})