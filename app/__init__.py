#!/usr/bin/env python
#-*- coding:utf-8 -*-
''''' 
Created on  
@author: zhuangyan 
'''
#-*- coding:utf-8 -*-

import os

from flask import Flask, request, jsonify
from flask_jwt import JWT
from flask_pymongo import PyMongo
# from flask_cors import CORS
from flask_uploads import UploadSet, IMAGES, configure_uploads

from settings import Config

mongo = PyMongo()
avatars = UploadSet('AVATAR')
tmpfiles = UploadSet('TMPFILE')

def create_app():
    """
    Flask Application Factory that takes configuration settings and returns
    a Flask application.
    """
    # initalize instance of Flask application
    app = Flask(__name__)

    app.config.from_object(Config)


    mongo.init_app(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        if request.method == 'OPTIONS':
            response.headers['Access-Control-Allow-Methods'] = 'DELETE, GET, POST, PUT'
            headers = request.headers.get('Access-Control-Request-Headers')
            if headers:
                response.headers['Access-Control-Allow-Headers'] = headers
        return response
    from app.auth import Auth
    auth = Auth()
    jwt = JWT(app, auth.authenticate, auth.identity)

    @jwt.auth_response_handler
    def response_handler(access_token, identity):
        data = {
            "result": "y",
            "msg": "",
            "data": {
                "token": access_token.decode('utf-8'),
                "is_admin": identity.is_admin,
                "userid": identity.id,
                "username": identity.username,
                "avatar": identity.avatar
            }
        }
        return jsonify(data)



    app.config['UPLOADED_AVATAR_DEST'] = os.path.dirname(os.path.abspath(__file__)) +"/_upload/avatars/"
    app.config['UPLOADED_TMPFILE_DEST'] = os.path.dirname(os.path.abspath(__file__)) +"/_upload/temps/"
    app.config['UPLOADED_AVATAR_ALLOW'] = IMAGES
    configure_uploads(app, avatars)
    configure_uploads(app, tmpfiles)


    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/_api')
    # register 'main' blueprint with Flask application
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    # register 'auth' blueprint with Flask application
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')



    return app
