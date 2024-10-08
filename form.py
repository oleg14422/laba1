from flask_wtf import FlaskForm
from wtforms import  SubmitField, StringField
from wtforms.validators import DataRequired


class MyForm(FlaskForm):
    text = StringField(validators=[DataRequired()])
    submit = SubmitField('Calculate')
