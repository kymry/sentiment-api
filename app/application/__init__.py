from flask import Flask
from .config import Config


def create_app():

	app = Flask(__name__)
	app.config.from_object(Config)
	from .models import db, migrate
	db.init_app(app)
	migrate.init_app(app, db)

	with app.app_context():
		from .routes import bp
		app.register_blueprint(bp)

		return app
