from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager



database = SQLAlchemy()
DB_NAME =  "database.db"

def create_app(): #define function
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "DEMO-KEY-HERE"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    database.init_app(app)
    
 
    from .views import views
    from .auth import auth
    

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from . import models
    from .models import User
    with app.app_context():
        database.create_all() #creating database

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' #redirecting user to login if they are not login
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
     return User.query.get(int(id))

    return app


  