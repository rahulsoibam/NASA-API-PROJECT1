#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os
from flask import Flask, render_template, request, Response
from flask_restplus import Api, Resource, fields, reqparse
from config import Config
from API import response_request_nasa_api
from modules import request_nasa_api
# BASIC APP CONFIG
##################

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['DEBUG'] = True
api = Api(app
        , version=Config.API_VERSION
        , title=Config.API_TITLE
        , description=Config.API_DESCRIPTION
        , default=Config.API_DEFAULT
        , default_label=Config.API_DEFAULT_LABEL)
        
@app.route(Config.INDEX_URL, methods=['GET'])
def app_body():
    return render_template('index.html')

# ENTRY POINT
@app.route('/apiModuleNasa')
def apiModuleNasa():
    API_TOKEN = request.args.get('API_TOKEN')
    response = response_request_nasa_api(API_TOKEN)
    return response
#
# API → ENTRY POINT
###################
@api.route('/apiModuleNasa?API_TOKEN=<string:API_TOKEN>')
class apiModule(Resource):
    def get(self, API_TOKEN):
        response = response_request_nasa_api(API_TOKEN)
        return response

# APP RUN SETTINGS
##################
if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0',port=5005, threaded=True)
    

