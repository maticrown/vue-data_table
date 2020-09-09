from flask import Flask, render_template, json

import os
import socketio
import eventlet
import http.server
import socketserver
import threading


'''from .emanesh_routing_pb2 import Measurement_emane_emanesh_routing_transport
from .emanesh_routing_pb2 import Measurement_emane_emanesh_routing_mac
from .emanesh_routing_pb2 import Measurement_emane_emanesh_routing_phy

import otestpoint.toolkit.logger as Logger
from otestpoint.interface import Probe
from otestpoint.interface.measurementtable_pb2 import MeasurementTable

import time
import ntplib

import subprocess
import json
import re
'''

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return 'Matanel Crown is a programmer, subscribe to him'

@app.route('/test')
def test():
    my_dict = { "layer1": "phy","layer2": "mac","layer3":"transport" }
    return json.dumps(my_dict)

@app.route('/serve_socketio')
def serve_socketio():
#    sio = socketio.Server(cors_allowed_origins='*') # NOT SECURE!!!! DO NOT US$
#    app = socketio.WSGIApp(sio)
#    @sio.event
#    def connect(sid, environ):
#        print('Someone (GUI) logged in ')
#    @sio.event
#    def number_recv(sid, number):
#        print("Number is ", number)
#        port = int(os.environ.get('PORT', 3000))
#        eventlet.wsgi.server(eventlet.listen(('0.0.0.0', port)), app)

#    t2 = threading.Thread(target=serve_socketio)
#    t2.start()

# Run a system command to open google chrome with this
#    os.system('http://localhost')

#    return render_template('layout.html')

#@app.route('/probe')
#def probe():
    return render_template('layout.html')

@app.route('/table')
def table():
    return render_template('table.html')

@app.route('/dynamic-table')
def dynamic_table():
    return render_template('dynamic_table.html')

if __name__ == "__main__":
    print("server is running on localhost")
    #app.run(debug=True, host="10.99.0.1")
    app.run(debug=True)
