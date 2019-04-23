#!/usr/bin/env python3

from flask import Flask, request
from flask_restful import Resource, Api
import os
import json
import glob

app = Flask(__name__)
api = Api(app)
RootDir = '/var/restapp/conf'

class Root_Message(Resource):
    def get(self):
               return 'Welcome to test RestApi v0.1'

class Json_Objects(Resource):
    def get(self, zion):
        for current_directory,directories,files in os.walk(RootDir):
            for file in files:
                filePath = os.path.join(current_directory,file)
                with open(filePath,'rb') as f:
                    result = json.load(f)
                return json.dumps(result, indent=4, sort_keys=True)

api.add_resource(Root_Message, '/')
api.add_resource(Json_Objects, '/conf/<string:zion>')

if __name__ == '__main__':
     app.run()
