from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route("/aboutus")
def aboutus():
    return "about us page"


@views.route("/services")
def services():
    return "service us page"

@views.route("/contact")
def contact():
    return "contact us page"

@views.route("/blog")
def blog():
    return "blog us page"