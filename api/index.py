from sanic import Sanic
from sanic.response import json

app = Sanic(__name__)


@app.route('/')
@app.route('/<path:path>')
async def index(request, path=""):
    return json({'hello': path})
