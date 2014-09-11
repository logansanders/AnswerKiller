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

admin_login_manager = LoginManager()
@admin_login_manager.user_loader
def load_user(username):
    the_user = user.Account.query.filter_by(username=username)
    if the_user.permission_level > 0:
        return the_user
    return None

@admin_login_manager.unauthorized_handler
def unauthorized():
    return 'PLease log in'

admin_login_manager.init_app(app)

from answerkiller.views.admin_views import admin_bp
app.register_blueprint(admin_bp)
