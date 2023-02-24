from flask import Flask
from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy()
DB_NAME =  "database.db"
def create_app(): #define function
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "DEMO-KEY-HERE"
    app.config['SQLACHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.init_app(app)
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    return app