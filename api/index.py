from os import path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


def _render_page(page_name: str):
    with open(path.join('data', 'src', 'pages', f'{page_name}.html')) as page:
        return page.read()


@app.get("/", response_class=HTMLResponse)
def read_root():
    return _render_page('home')
