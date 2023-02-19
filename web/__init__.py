from flask import Flask

def create_app(): #define function
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "DEMO-KEY-HERE"

    return app