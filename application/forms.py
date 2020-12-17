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

#REGISTER
class RegisterForm(Form):
    name = StringField('name',validators=[
        DataRequired(message='Name is required'),
        Length(min=2,max=20)
        ])
    lastname = StringField('lastname',validators=[
        DataRequired(message='Lastname is required'),
        Length(min=2,max=20)
        ])
    email = StringField('correo', validators=[InputRequired(),
    Email()
    ,Length(min=7,max=50,
    message='El correo debe estar entre 7 y 40 caracteres')])

    password = PasswordField('Contrasena',validators= [InputRequired(), 
    #EqualTo('password1', 
    #message='Las contrasenas deben coincidir'),    
    Length(min=8,max=20,message='Contraseña debe estar entre 8 y 20 caracteres')])

    #password1 = PasswordField('Contrasena1',validators= [     
    #Length(min=8,max=20,message='Contraseña debe estar entre 8 y 20 caracteres')])
    
    captcha = RecaptchaField()

# # FORM RECOVER
class RecoverForm(Form):
     email = StringField('email',[
        DataRequired(message='Email required'),
        Length(min=8,max=20)
        ])
# # FORM ADD BLOG
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


