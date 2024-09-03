from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from os import path
app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def read_root():
    html_content = open(path.join('data', 'home.html')).read()
    return html_content
