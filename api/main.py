from os.path import join

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def read_root():
    with open(join('pages', 'home.html'), 'r') as f:
        html_content = f.read()
    return html_content
