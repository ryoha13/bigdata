from flask import render_template
from . import auth


@auth.route('/login')
def login():
    return render_template('auth/login.html')


@auth.route('/logout')
def logout():
    return 'logout'


@auth.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('auth/register.html')
