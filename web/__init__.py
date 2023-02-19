from flask import Flask

def create_app(): #define function
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "DEMO-KEY-HERE"

    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    return app