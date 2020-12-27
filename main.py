from sanic import Sanic
from sanic import response
from sanic.log import logger
from controller.url_controller import blueprint as url_blueprint

app = Sanic("Shorten URL")

app.blueprint(url_blueprint)

app.run(host="0.0.0.0", port=8000, debug=True)
