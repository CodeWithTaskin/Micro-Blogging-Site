import sys
from flask_sqlalchemy import SQLAlchemy
from src.exception import MyException

def create_app(app : object):
    try:
        db = SQLAlchemy(app)
        class Users(db.Model):
            id = db.Column(db.Integer, primary_key=True)
            name = db.Column(db.String(100), nullable=False)
            phone = db.Column(db.Integer, nullable=False, unique=True)
            email = db.Column(db.String(100), unique=True, nullable=False)
            password = db.Column(db.String(20), nullable=False)
            avatar = db.Column(db.String(500))
            
        with app.app_context():
            db.create_all()
        
        return (db, Users)
    
    except Exception as e:
        raise MyException(e, sys) from e