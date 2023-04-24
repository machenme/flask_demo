from flask import Flask, render_template

import sys
import os

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


app = Flask(__name__, static_url_path="", static_folder=resource_path(
    'static'), template_folder=resource_path("templates"))

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/static')
def static_file():
    return app.send_static_file('style.css')

if __name__=='__main__':
    app.run()