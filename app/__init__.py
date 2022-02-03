# Intializing things
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

#init the app
app = Flask(__name__)

#link our config to oour app
app.config.from_object(Config)

# init my Login Manager
login = LoginManager(app)
# This is where you will be sent if you are not logged
# into trying to go to a login required page
login.login_view='login'

# Do inits for database stuff
db = SQLAlchemy(app)
migrate = Migrate(app, db)



from app import routes, models
