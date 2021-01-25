#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    name = "Hello World"
    return name

@app.route('/good')
def good():
    name = "Good"
    return name

if __name__ == "__main__":
    app.run(host='localhost', port=3000,threaded=True)