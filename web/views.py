from flask import Blueprint

views = Blueprint("views", __name__)

@views.route('/')
def home():
    return "hello from home view"