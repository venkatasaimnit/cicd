# -*- coding: utf-8 -*-
"""
Created on Fri May 28 10:29:10 2021

@author: venka
"""

import flask
from flask import Flask,request,jsonify
from gevent.pywsgi import WSGIServer
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/hello",methods=['POST','GET'])
def hello():
    return "Hello World"

if __name__=="__main__":
    port = 5000
    http_server = WSGIServer(("0.0.0.0",port),app)
    print("running on port{0}".format(port))
    http_server.serve_forever()