# models.py
import flask_sqlalchemy
from app import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #user = db.Column(db.String(100))
    text = db.Column(db.String(250))
    
    def __init__(self, a):
        self.text = a
        
    def __repr__(self):
        return '<Message Text: %s>' % self.text
        
'''
class Usps(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(120))
    
    def __init__(self, a):
        self.address = a
        
    def __repr__(self):
        return '<Usps address: %s>' % self.address 
'''
