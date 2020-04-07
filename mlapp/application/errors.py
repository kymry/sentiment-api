from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES


def error_response(status_code, message=None):
    output = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
    if message:
        output['message'] = message
    response = jsonify(output)
    response.status_code = status_code
    return response
