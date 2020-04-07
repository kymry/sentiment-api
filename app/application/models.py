from sqlalchemy import func
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import datetime


db = SQLAlchemy()
migrate = Migrate()


class Question(db.Model):
	''' Store the randomly generated questions that are displayed to the user
	'''
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	text = db.Column(db.Text, nullable=False)

	def __repr__(self):
		return '<Question {} is: {}>'.format(self.id, self.text)

	@staticmethod
	def random():
		''' Queries a random row and returns the corresponding question '''
		question = Question.query.order_by(func.random()).first().text
		return question


class Sentiment(db.Model):
	''' User generated sentiments that will be used to re-train the Keras model
	'''
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	text = db.Column(db.Text, nullable=False)
	sentiment = db.Column(db.Boolean, nullable=False)
	correct = db.Column(db.Boolean, nullable=False)
	date = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)

	@staticmethod
	def get_accuracy_data():
		accuracy = Sentiment.query.with_entities(Sentiment.correct, Sentiment.date).all()
		return accuracy

	def __repr__(self):
		return '<Question {} is: {}>'.format(self.id, self.text)
