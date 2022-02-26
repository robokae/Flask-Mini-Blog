from flask import render_template
from . import main
from .forms import LoginForm, RegisterForm
from .. import db
from ..models import User

@main.route('/')
def landing():
    return render_template('landing.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        # add user to the database
        user = User(username=username, password=password)

        db.session.add(user)
        db.session.commit()

    return render_template('register.html', form=form)