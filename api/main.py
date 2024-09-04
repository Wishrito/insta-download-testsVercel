from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from os.path import join
app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def read_root():
    with open(join('pages', 'home.html'), 'r') as f:
        html_content = f.read()
    return html_content
