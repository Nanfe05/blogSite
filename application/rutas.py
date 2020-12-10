# API ROUTES 
from flask import Flask,Blueprint,jsonify,request
from application.forms import LoginForm,RegisterForm,RecoverForm,AddBlogForm


blog_api=Blueprint('blog_api',__name__)

@blog_api.route('/api/login',methods=['POST'])
def login():
    form = LoginForm(request.form)
    if form.validate():
        return jsonify(type='success',msg='Ingreso exitoso!')
    return jsonify(type='error',msg='Error en el login!')

# /api/register/
@blog_api.route('/api/register',methods=['POST'])
def register():
    form = RegisterForm(request.form)
    if form.validate():
        return jsonify(type='success',msg='Registro exitoso!')
    return jsonify(type='error',msg='Error en el Registro!')

@blog_api.route('/api/recoverpassword',methods=['POST'])
def recover():
    form = RecoverForm(request.form)
    if form.validate():
        return jsonify(type='success',msg='Recuperacion Exitosa!')
    return jsonify(type='error',msg='No se puede recupear la contrasena!')

@blog_api.route('/api/addblog',methods=['POST'])
def add_blog():
    form = AddBlogForm(request.form)
    if form.validate():
        return jsonify(type='success',msg='Blog Agregado exitosamente!')
    return jsonify(type='error',msg='No se puede agregar el blog!')

@blog_api.route('/api/blogs',methods=['GET'])
def get_blogs():
    return jsonify(type='blog',msg='Te estamos enviando todos los blogs ....')