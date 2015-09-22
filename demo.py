# -*- coding: UTF-8 -*-
__author__ = 'douglas_bonafe'

import flask
from flask.views import MethodView

app = flask.Flask(__name__)

class View(flask.views.MethodView):

    def get(self):
        return "Hello world!"

app.add_url_rule('/', view_func=View.as_view('main'))


app.debug = True
app.run()