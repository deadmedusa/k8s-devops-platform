from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import httpx
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

BACKEND_URL = os.getenv("BACKEND_URL", "http://backend-service:8000")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    async with httpx.AsyncClient() as client:
        info = await client.get(f"{BACKEND_URL}/info")
        hello = await client.get(f"{BACKEND_URL}/hello")

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "info": info.json(),
            "hello": hello.json()
        }
    )
