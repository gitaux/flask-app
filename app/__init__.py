# -*- coding: utf-8 -*-
# app/__init__.py

from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

from config import app_config

cp = CSRFProtect()
db = SQLAlchemy()
lm = LoginManager()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    cp.init_app(app)
    db.init_app(app)
    lm.init_app(app)
    lm.login_message = "You must sign up to access this page."
    lm.login_view = "auth.signin"

    migrate = Migrate(app, db)
    from app import models

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    return app
