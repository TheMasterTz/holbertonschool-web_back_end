#!/usr/bin/env python3
""" Module of Index views
"""
from os import abort
from flask import Flask, jsonify
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ GET /api/v1/status
    Return:
      - the status of the API
    """
    return jsonify({'status': 'OK'})


@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def unauthorized() -> str:
    """ endpoint to testing (unauthorized) 401 error handler """
    abort(401)


