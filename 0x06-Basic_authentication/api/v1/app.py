"""
    _summary_
"""
from os import getenv
from flask import Flask, jsonify


app = Flask(__name__)


@app.errorhandler(401)
def unauthorized(error) -> str:
    """error handler for (unauthorized) 401 status code"""
    return jsonify({"error": "Unauthorized"}), 401


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
