from flask import Flask
# from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,Form
from wtforms.validators import DataRequired,Length
app = Flask(__name__)

app.config['SECRET_KEY'] = 'grupoC'
# FORM LOGIN
class LoginForm(Form):
    email = StringField('email',[
        DataRequired(message='Email required'),
        Length(min=6,max=20)
        ])
    password = PasswordField('password',validators=[
        DataRequired(message='Password required'),
        Length(min=6,max=12),
        ])


# # FORM REGISTER
class RegisterForm(Form):
    name = StringField('name',[
        DataRequired(message='Name is required'),
        Length(min=6,max=20)
        ])
    lastname = StringField('lastname',[
        DataRequired(message='Name is required'),
        Length(min=6,max=20)
        ])
    email = StringField('email',[
        DataRequired(message='Email required'),
        Length(min=6,max=20)
        ])
    password = PasswordField('password',validators=[
        DataRequired(message='Password required'),
        Length(min=6,max=12),
        ])

# # FORM RECOVER
class RecoverForm(Form):
     email = StringField('email',[
        DataRequired(message='Email required'),
        Length(min=8,max=20)
        ])
# # FORM ADD BLOG
class AddBlogForm(Form):
    name = StringField('name',[
        DataRequired(message='Name is required'),
        Length(min=6,max=20)
        ])
    subject = StringField('subject',[
        DataRequired(message='subject is required'),
        Length(min=6,max=20)
        ])


