from flask_wtf import FlaskForm
from wtforms import StringField, TelField, SubmitField, EmailField
from wtforms.validators import InputRequired, EqualTo

class SignUpForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])
    phoneno = TelField('Phone Number', validators=[InputRequired()])
    address = StringField('Address', validators=[InputRequired()])
    submit = SubmitField('Submit')