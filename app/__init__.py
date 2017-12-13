from flask import Flask, render_template
from config import SECRET_PASSWORD

app = Flask(__name__, static_folder='react_app')
app.secret_key = SECRET_PASSWORD

import api


@app.route('/')
def index():
    return render_template('index.html')
