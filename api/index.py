from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from os import path
app = FastAPI()


def render_page(page_name: str):
    page = open(path.join('data', f'{page_name}.html')).read()
    return page

@app.get("/", response_class=HTMLResponse)
def read_root():
    return render_page('home')
