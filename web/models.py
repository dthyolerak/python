from . import database
from flask_login import UserMixin

class User(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    email = database.Column(database.String(170), unique=True)
    password = database.Column(database.String(500))
    first_name = database.Column(database.String(150))
    