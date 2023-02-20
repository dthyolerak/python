from flask import Blueprint, render_template, request, flash

auth = Blueprint("auth", __name__)

@auth.route("login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        Email = request.form.get('Email')
        Password = request.form.get('Password')

        if len( Password) < 7:
            flash('Password must be 3 character above', category="error")
        elif len(Email) < 4:
            flash('We don\'t allow this type of email', category="error")
        else:
            flash('Count has been created successful', category="success")
    return render_template('login.html')

@auth.route("/register", methods=['GET','POST'])
def register():
    if request.method == "POST":
        FullName = request.form.get('FullName')
        Email = request.form.get('Email')
        Password = request.form.get('Password')
        PhoneNumber = request.form.get('PhoneNumber')

        if len(FullName) < 4:
            flash('Full name must be 3 character above', category="error")
        elif len( Password) < 7:
            flash('Password must be 7 character above', category="error")
        elif len(Email) < 4:
            flash('We don\'t allow this type of email', category="error")
        elif len(PhoneNumber) != 10:
            flash('invalide phone number', category="error")
        else:
            flash('Count has been created successful', category="success")
    return render_template('register.html')

@auth.route("/logout")
def logout():
    return "hello  from logout"
