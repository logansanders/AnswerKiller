from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

app = Flask(import_name=__name__,
            static_folder='templates/admin', static_url_path='')
app.config.from_pyfile('../etc/conf/debug.cfg')
from werkzeug import SharedDataMiddleware
import os
app.wsgi_app = SharedDataMiddleware(app.wsgi_app,
                                {'/css': os.path.join(os.path.dirname(__file__),
                                 'tempaltes/admin/css')})

db = SQLAlchemy(app)

from answerkiller.models import user
admin_login_manager = LoginManager()


@admin_login_manager.user_loader
def load_user(username):
    print 'loading user'
    the_user = user.Account.query.filter_by(username=username).first()
    if the_user.permission_level > 0:
        return the_user
    return None


@admin_login_manager.unauthorized_handler
def unauthorized():
    return 'PLease log in'

admin_login_manager.init_app(app)

from answerkiller.views.admin_views import admin_bp
app.register_blueprint(admin_bp)
