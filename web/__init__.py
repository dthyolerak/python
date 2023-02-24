from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

database = SQLAlchemy()
DB_NAME =  "database.db"

def create_app(): #define function
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "DEMO-KEY-HERE"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    database.init_app(app)
    # app.__init__(app)
    from .views import views
    from .auth import auth
    

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from . import models

    with app.app_context():
        database.create_all()
    return app


  