
#from myapp.models import db, User 
import functools

from flask import (
Blueprint, flash, g, redirect,render_template,request,session,url_for
)
from werkzeug.security import check_password_hash, generate_password_hash



#auth = Blueprint('auth', __name__ , template_folder='templates')
auth = Blueprint('auth', __name__ )


@auth.route('/login')
def login():
    return render_template('auth/login.html')


@auth.route("/register")
def register():
	return render_template('auth/register.html')	
