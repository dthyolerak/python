from flask import Blueprint

views = Blueprint("views", __name__)

@views.route('/')
def home():
    return "hello from home view"

@views.route("/aboutus")
def aboutus():
    return "about us page"


@views.route("/service")
def service():
    return "service us page"

@views.route("/contact")
def contact():
    return "contact us page"

@views.route("/blog")
def blog():
    return "blog us page"