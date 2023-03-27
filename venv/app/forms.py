from flask_wtf import FlaskForm
from wtforms import StringField, TelField, SubmitField, EmailField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, EqualTo

class SignUpForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    phoneno = TelField('Phone Number', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_pass = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords Must Match')])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    body = TextAreaField('Body', validators=[DataRequired()])
    image_url = StringField('Image URL')
    submit = SubmitField('Create Post')

class SearchForm(FlaskForm):
    search_term = StringField('Search Term')
    submit = SubmitField('Search')
