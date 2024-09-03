from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def read_root():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My FastAPI App</title>
    </head>
    <body>
        <h1>Hello, world!</h1>
        <p>This is a simple HTML page served by FastAPI.</p>
    </body>
    </html>
    """
    return html_content
