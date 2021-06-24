from flask import Flask
from flask.templating import render_template
from config import Config
from .api.routes import api
from .site.routes import site
from .authentication.routes import auth
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db as root_db, login_manager, ma
#from drone_inventory.models(if moving the .py files)
from flask_cors import CORS
from flask.json import JSONEncoder
from drone_inventory.helpers import JSONEncoder


app = Flask(__name__)

app.config.from_object(Config)
app.register_blueprint(api)
app.register_blueprint(site)
app.register_blueprint(auth)

root_db.init_app(app)
migrate = Migrate(app, root_db)
login_manager.init_app(app)
ma.init_app(app)

app.json_encoder = JSONEncoder

import models

CORS(app)
