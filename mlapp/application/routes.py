from flask import Blueprint, jsonify, request, Response
from .model.model import predict, get_true_sentiment
from .errors import error_response
from .models import Question, Sentiment, db


bp = Blueprint('api', __name__)


@bp.route('/sentiment', methods=['POST'])
def get_sentiment():
	data = request.get_json()
	if data is not None and len(data["review"]) > 0:
		prediction = predict(data["review"])
		return jsonify(prediction)
	return error_response(400, 'Review must be at least one character')


@bp.route('/prediction', methods=['POST'])
def add_sentiment():
	data = request.get_json()
	if data is not None:
		sentiment = get_true_sentiment(data['prediction'], data['submit_correct'], data['submit_incorrect'])
		entry = Sentiment(text=data['review'], sentiment=sentiment, correct=True)
		db.session.add(entry)
		db.session.commit()
		return Response(response='success', status=200)
	return error_response(400, 'Something went wrong')


@bp.route('/question', methods=['GET'])
def get_question():
	return jsonify(Question.random())
