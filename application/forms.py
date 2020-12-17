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
        Length(min=6,max=50)
        ])
    password = PasswordField('password',validators=[
        DataRequired(message='Password required'),
        Length(min=6,max=12),
        ])


# # FORM REGISTER
class RegisterForm(Form):
    name = StringField('name',[
        DataRequired(message='Name is required'),
        Length(min=2,max=20)
        ])
    lastname = StringField('lastname',[
        DataRequired(message='Lastname is required'),
        Length(min=2,max=20)
        ])
    email = StringField('email',[
        DataRequired(message='Email required'),
        Length(min=6,max=50)
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
## FORM ADD BLOG
class AddBlogForm(Form):
    title = StringField('title',[
        DataRequired(message='Title is required'),
        Length(min=1,max=30)
        ])
    subject = StringField('subject',[
        DataRequired(message='subject is required'),
        Length(min=1,max=20)
        ])
    content = StringField('content',[
        DataRequired(message='subject is required'),
        Length(min=1,max=250)
        ])
## FORM ADD BLOG
class AddCommentForm(Form):
    id = StringField('id',[
        DataRequired(message='ID is required'),
        Length(min=1,max=10)
        ])
    comment = StringField('comment',[
        DataRequired(message='comment is required'),
        Length(min=1,max=100)
        ])


