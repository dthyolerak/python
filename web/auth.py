from flask import Blueprint

auth = Blueprint("auth", __name__)

@auth.route("login")
def login():
    return "hello from login page"

@auth.route("/register")
def register():
    return "hello from registe"

@auth.route("/logout")
def logout():
    return "hello  from logout"
