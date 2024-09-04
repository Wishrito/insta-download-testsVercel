from os.path import join

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def read_root():
    with open(join('pages', 'home.html'), 'r') as f:
        html_content_list = f.readlines()
    html_content = ""
    for line in html_content_list:
        if line.startswith('<link rel="stylesheet"'):
            line = f"<link rel=\"stylesheet\" href=\"{join('..', 'src', 'css', 'home.css')}\">"
            html_content += line
    return html_content
