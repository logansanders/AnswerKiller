from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager


app = Flask(import_name=__name__, static_folder='views/static',
            template_folder='views')
app.config.from_pyfile('..\etc\conf\debug.cfg')

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

from answerkiller import routes
