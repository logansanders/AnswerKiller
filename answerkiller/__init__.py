from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
<<<<<<< HEAD

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://answerkiller:killer@localhost/answerkiller'
db = SQLAlchemy(app)
=======
from flask.ext.login import LoginManager


app = Flask(import_name=__name__, static_folder='views/static',
            template_folder='views')
app.config.from_pyfile('..\etc\conf\debug.cfg')

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

from answerkiller import routes
>>>>>>> 8f18acf6e40627af1f1a40326f87b1436ade4a08
