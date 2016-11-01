"""This module holds all views controls for...

ecomap project.
"""

from app import app
from connection import get_images
from flask import render_template, jsonify


@app.route("/")
def index():
    """That is the main index.html."""
    return render_template('index.html')


@app.route("/api/all_images")
def all_images():
    """Funcion return list of images in the system."""
    local_images = get_images()
    responce = jsonify(local_images)
    return responce

if __name__ == '__main__':
    app.run()
