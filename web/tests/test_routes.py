import pytest
from httpx import AsyncClient, ASGITransport
from fastapi.responses import HTMLResponse

from main import app
from routers import chat, auth

routes_lst = chat.router.routes + auth.router.routes


@pytest.mark.asyncio
async def test_templates():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url='http://127.0.0.1:8000') as client:
        for r in routes_lst:
            if r.response_class == HTMLResponse:
                response = await client.get(r.path)
                assert response.status_code == 200



