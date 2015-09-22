# -*- coding: UTF-8 -*-
__author__ = 'douglas_bonafe'

import flask
from flask.views import MethodView
import os
app = flask.Flask(__name__)

# when we use the flask.flash we need to create a secret_key
# But don't do this!
app.secret_key = "bacon"

class View(flask.views.MethodView):

    def get(self):
        return flask.render_template('index.html')

    def post(self):
        result = eval(flask.request.form['expression'])
        flask.flash(result)
        return self.get()
        ## expression is tha name of the field

app.add_url_rule('/', view_func=View.as_view('main'), methods=['GET', 'POST'])


app.debug = True
app.run()