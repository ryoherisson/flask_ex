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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            print('ユーザー名が異なります')
        elif request.form['password'] != app.config['PASSWORD']:
            print('パスワードが異なります')
        else:
            return redirect('/')
    return render_template('entries/login.html')

@app.route('/logout')
def logout():
    return redirect('/')