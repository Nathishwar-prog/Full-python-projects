from flask import jsonify


def error_response(message, status_code):
    """Create a standard error response"""
    return jsonify({"error": message}), status_code