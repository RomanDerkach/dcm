#!/usr/bin/python
"""This module holds all views controls for...

FreshFishproject.
"""
import connection
from app import app
from flask import render_template, jsonify, request


@app.route("/")
def index():
    """That is the main index.html."""
    return render_template('index.html')


@app.route("/api/all_images")
def all_images():
    """Funcion return list of images in the system."""
    local_images = connection.get_images()
    responce = jsonify(local_images), 200
    return responce


@app.route("/api/run_container", methods=['POST'])
def run_container():
    """Function get image name from request and run container."""
    data = request.get_json()
    connection.run_container(data.get('image_name_tag'))
    responce = jsonify(), 200
    return responce


@app.route("/api/del_image", methods=['DELETE'])
def del_image():
    """Function will delete image by it`s name."""
    data = request.get_json(force=True)
    connection.del_image(data.get('image_name_tag'))
    responce = jsonify(), 200
    return responce


@app.route("/api/all_containers", methods=['GET'])
def all_containers():
    """Function will retuln all the containers."""
    local_containers = connection.get_containers()
    responce = jsonify(local_containers), 200
    return responce


if __name__ == '__main__':
    app.run()
