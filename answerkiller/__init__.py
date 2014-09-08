from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager


app = Flask(import_name=__name__, static_folder='views/static')
app.config.from_pyfile('../etc/conf/debug.cfg')
app.url_map.default_subdomain = "admin"

db = SQLAlchemy(app)
from answerkiller.models import user
from answerkiller.models import order
from answerkiller.models import image
from answerkiller.models import course

login_manager = LoginManager()
login_manager.init_app(app)

from answerkiller.views.admin_views import admin_bp
app.register_blueprint(admin_bp)