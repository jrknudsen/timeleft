from datetime import datetime
from app import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee = db.Column(db.String(240), index=True, unique=True)
    #photo = 
    enddate = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    posts = db.relationship('Post', backref='employee_name', lazy='dynamic')

    def __repr__(self):
        return '<Employee {}>'.format(self.employee)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(240), index=True)
    body = db.Column(db.String(1240), index=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))

    def __repr__(self):
        return '<Name {}>'.format(self.name)

    def __repr__(self):
        return '<Body {}>'.format(self.body)