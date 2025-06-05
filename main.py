from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_home(request: Request):
    dynamic_data = {
        "request": request,
        "title": "Welcome to Rani Rituals",
        "tagline": "Your self-care sanctuary for the modern desi girl.",
        "cta": "Explore Your Rituals"
    }
    return templates.TemplateResponse("home.html", dynamic_data)
