from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField
from wtforms.validators import DataRequired,Length,Email,EqualTo

class Registration_Form(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),Length(min=2,max=50)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    cnfrm_password = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo(password, message='Password Must Match')])

    submit = SubmitFeild('Sign Up')

class Registration_Form(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),Length(min=2,max=50)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    cnfrm_password = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo(password, message='Password Must Match')])

    submit = SubmitFeild('Sign Up')