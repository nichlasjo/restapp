#!/usr/bin/env python3

from flask import Flask, request
from flask_restful import Resource, Api
import os
import json
import sys

app = Flask(__name__)
api = Api(app)
rootdir = 'conf'

class Root_Message(Resource):
    def get(self):
        return 'Welcome to test RestApi v0.1'

class Dir_Objects(Resource):
    def get(self, list):
        output = {}
        current_path = str(request.path)[1:].split("/")
        output["current_path"] = current_path[0]
        return output

class File_Objects(Resource):
    def get(self, data):
        output = {}
        current_path = str(request.path)[1:].split("/")
        output["current_path"] = current_path[1]
        #open json object in dir (output)
        return output

api.add_resource(Root_Message, '/')
api.add_resource(Dir_Objects, '/<string:list>')
api.add_resource(File_Objects, '/conf/<string:data>')

if __name__ == '__main__':
     app.run()
