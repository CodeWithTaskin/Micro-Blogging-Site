from flask import (
    Flask,
    redirect,
    url_for,
    render_template,
    json,
    jsonify,
    send_file,
    request,
    make_response,
    
)
from src.constants import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

