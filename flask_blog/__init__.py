# flask_blog/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Flask application本体作成
app = Flask(__name__)
app.config.from_object('flask_blog.config')

db = SQLAlchemy(app)

from flask_blog.views.entries import entry

app.register_blueprint(entry, url_prefix='/users')

from flask_blog.views import views