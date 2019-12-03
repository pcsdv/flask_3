
import os
from flask import Flask
from flaskr.config import Config


def create_app(config_class=Config ):
	app = Flask(__name__)
	app.config.from_object(Config)

	from flaskr.main.routes import main
	from flaskr.auth.routes import auth

	# and register blueprints
	app.register_blueprint(main)
	app.register_blueprint(auth)

	return app
