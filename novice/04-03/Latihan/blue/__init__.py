from flask import Flask

app = Flask(__name__)

from blue.api.routes import mod
from blue.site.routes import site

app.register_blueprint(site.routes.mod)
app.register_blueprint(api.routes.mod, url_prefix='/api')