# flask_blog/__init__.py

from flask import Flask

# Flask application本体作成
app = Flask(__name__)

import flask_blog.views