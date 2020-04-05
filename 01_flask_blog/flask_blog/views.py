# flask_blog/views.py
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for

from flask_blog import app

@app.route('/')
def show_entries():
    # index.htmlでrendering
    return render_template('entries/index.html')

