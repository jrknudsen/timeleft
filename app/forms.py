from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
from wtforms import StringField, SubmitField, DateField, TextAreaField
from wtforms.validators import DataRequired
from app.models import Post, Employee


class EmployeeForm(FlaskForm):
    employee = StringField('Name', validators=[DataRequired()])
    ##photo = FileField('Photo', validators=[FileRequired()])
    enddate = DateField('When is the employee having his/her last day', validators=[DataRequired()])
    submit = SubmitField('Submit')

class MessageForm(FlaskForm):
    name = StringField('Navn', validators=[DataRequired()])
    body = TextAreaField('Melding', validators=[DataRequired()])
    submit = SubmitField('Send')