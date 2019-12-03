
from flask import Blueprint,render_template,redirect, url_for,request,flash

#from myapp.models import db, User 
from flask import current_app as app

main = Blueprint('main', __name__ , template_folder='templates', static_folder='static', static_url_path='/static/main')
#main = Blueprint('main', __name__ )


@main.route("/")
def index():
	return render_template('main/index.html')	

@main.route("/home")
def home():
	return render_template('main/home.html')	
