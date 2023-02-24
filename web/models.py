from . import database
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    email = database.Column(database.String(170), unique=True)
    password = database.Column(database.String(500))
    first_name = database.Column(database.String(150))

class  Post(database.Model):
    id = database.Column(database.Integer, primary_key = True)
    user_id = database.Column(database.Integer, id.ForeignKey('user.id'))
    title = database.Column(database.String(500))
    description = database.Column(database.String(3000))
    img_location =  database.Column(database.String(1000))
    date = database.Column(database.DateTime(timezome =True), default = func.now())