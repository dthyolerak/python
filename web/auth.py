from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import database
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
auth = Blueprint("auth", __name__)

@auth.route("login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        Email = request.form.get('Email')
        password = request.form.get('password')
        user = User.query.filter_by(email=Email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('welcome to dashbord', category='success')
                redirect(url_for('views.home'))
            else:
                flash('incorrect password', category='error')
        else:
            flash('incorrect email', category='error')
       
    return render_template('login.html')

@auth.route("/register", methods=['GET','POST'])
def register():
    if request.method == "POST":
        FullName = request.form.get('FullName')
        Email = request.form.get('Email')
        Password = request.form.get('Password')
        PhoneNumber = request.form.get('PhoneNumber')
        user_email = User.query.filter_by(email=Email).first()
        user_phone_number = User.query.filter_by(phone_number=PhoneNumber).first()
        if user_email:
            flash('Phone number arleady register by someone else', category="error")
            
        elif user_phone_number:
            flash('email arleady register by someone else', category="error")
        elif len(FullName) < 4:
            flash('Full name must be 3 character above', category="error")
        elif len( Password) < 7:
            flash('Password must be 7 character above', category="error")
        elif len(Email) < 4:
            flash('We don\'t allow this type of email', category="error")
        elif len(PhoneNumber) != 10:
            flash('invalide phone number', category="error")
        else:
           
            hashed_pwd = generate_password_hash(Password,method='sha256')
            user =  User(email= Email, full_name =FullName, password=hashed_pwd, phone_number = PhoneNumber)
            database.session.add(user)
            database.session.commit()
            flash('Count has been created successful', category="success")
            return redirect(url_for('auth.login'))
    return render_template('register.html')


@auth.route("/logout")
def logout():
    return "hello  from logout"
