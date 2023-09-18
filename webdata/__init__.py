from flask import Flask, render_template, url_for, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin, current_user
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from webdata.config import Config

app = Flask(__name__)
app.config.from_object(Config)

thisConfig = Config()

#mirip mysqli tadi, buka koneksi


app.config['SQLALCHEMY_DATABASE_URI'] = thisConfig.DB_URL
#template
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PERMANENT_SESSION_LIFETIME'] = 10800
app.config['SECRET_KEY'] = thisConfig.SECRET_KEY

loginManager = LoginManager(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)

from webdata.main.routes import main
from webdata.admin.routes import admin
app.register_blueprint(main, url_prefix='')
# app.register_blueprint(admin, url_prefix='/admin')

# import logging
# logging.basicConfig()
# logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

