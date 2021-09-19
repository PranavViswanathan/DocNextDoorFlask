# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 11:00:17 2021

@author: Pranav Viswanathan
"""

from flask import Flask, render_template
def create_app():
    app = Flask(__name__)
    @app.route('/')
    def hello_world():
        return render_template('home.html')
    return app
app = create_app()