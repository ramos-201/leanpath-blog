from starlette.applications import Starlette
from starlette.routing import Route
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

import configs


templates = Jinja2Templates(directory='src/templates')


async def index(request):
    return templates.TemplateResponse('index.html', {'request': request})


app = Starlette(
    routes=[
        Route('/', index),
    ],
    debug=configs.DEV,
)

app.mount('/static', StaticFiles(directory='src/static'), name='static')
