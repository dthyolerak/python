from . import database
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    email = database.Column(database.String(170), unique=True)
    password = database.Column(database.String(500))
    full_name = database.Column(database.String(150))
    phone_number =database.Column(database.String(14))
    date = database.Column(database.DateTime(timezone =True), default = func.now())
    post = database.relationship('Post')

class  Post(database.Model):
    id = database.Column(database.Integer, primary_key = True)
    user_id = database.Column(database.Integer, database.ForeignKey('user.id'))
    title = database.Column(database.String(500))
    description = database.Column(database.String(3000))
    img_location =  database.Column(database.String(1000))
    date = database.Column(database.DateTime(timezone =True), default = func.now())
    