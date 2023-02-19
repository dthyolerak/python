from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route("/aboutus")
def aboutus():
    return render_template('aboutus.html')


@views.route("/services")
def services():
    return render_template('services.html')

@views.route("/contact")
def contact():
    return render_template('contact.html')

@views.route("/blog")
def blog():
    return render_template('blog.html')