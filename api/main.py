from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def read_root():
    with open('../pages/home.html', 'r') as f:
        html_content = f.read()
    return html_content


@app.get("/items/{item_id}", response_class=HTMLResponse)
def read_item(item_id: int, q: str = None):
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Item {item_id}</title>
    </head>
    <body>
        <h1>Item ID: {item_id}</h1>
        <p>Query: {q}</p>
    </body>
    </html>
    """
    return html_content
