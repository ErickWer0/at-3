#!/usr/bin/env python3

from flask import Flask
from flask_login import LoginManager
from .models import User, UserBase


def create_app():
    app=Flask(__name__)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    app.secret_key='scjscdscsxskcsbchjbceff'

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return UserBase.sessions[user_id]
        #return UserBase.logins['user']

    from .files import files as files_blueprint
    app.register_blueprint(files_blueprint)
    return app

