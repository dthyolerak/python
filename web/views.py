from flask import Blueprint, render_template
from flask_login import login_required,  current_user
views = Blueprint("views", __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html")

@views.route('/admin')
@login_required
def admin():
    return "welcome to admin dashbord"

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