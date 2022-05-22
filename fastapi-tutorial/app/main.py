from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory=BASE_DIR/"templates")


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("./item.html", {"request": request, "id": id, "data": "FastAPI"})
