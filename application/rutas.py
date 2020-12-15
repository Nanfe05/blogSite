# API ROUTES 
import os
from flask import Flask,Blueprint,jsonify,request, session,redirect,url_for
from application.forms import LoginForm,RegisterForm,RecoverForm,AddBlogForm
from db.db import get_db,close_connection
import hashlib


blog_api=Blueprint('blog_api',__name__)


# /api/logout
@blog_api.route('/api/login',methods=['POST'])
def login():
    form = LoginForm(request.form)
    if form.validate():
        try:
            email = request.form.get('email')
            con = get_db()
            cursor = con.cursor()
            # Validar que el usuario existe
            query = "SELECT * FROM usuarios WHERE email='"+email+"'"
            cursor.execute(query)
            user_exists = cursor.fetchall()
            close_connection()
            if(len(user_exists) > 0):
                password_send= hashlib.sha256((request.form.get('password')+os.environ.get("SALT_PASSWORD")).encode()).hexdigest()
                password_real= user_exists[0][4]
                if(password_real == password_send):
                    session['user_email']=email
                    return redirect(url_for("blog"))
                    #return jsonify(type='success',msg='Ingreso exitoso!')
                else:
                    raise Exception("Usuario ya existe")    
            # Validar Password    
            else:
                raise Exception("Usuario ya existe")    
        except Exception as e:
            print(e)
            return jsonify(type='error',msg='Error en el login!')
    return jsonify(type='error',msg='Error en el login!')

# /api/logout/
@blog_api.route('/api/logout',methods=["GET"])
def logout():
    session.pop("user_email")
    return redirect(url_for("home"))

# /api/register/
@blog_api.route('/api/register',methods=['POST'])
def register():
    form = RegisterForm(request.form)
    # form.validate()
    # print(form.errors)
    if form.validate():
        try:
            email = request.form.get('email')
            con = get_db()
            cursor = con.cursor()
            ## CHECK IF EMAIL PREVIOUSLY EXISTS
            query = "SELECT email FROM usuarios WHERE email='"+email+"'"
            cursor.execute(query)
            user_exists = cursor.fetchall()
            if(len(user_exists)):
                close_connection()
                # Init session
                return jsonify(type='error',msg='Error al registrar usuario!')
                #return jsonify(type='success',msg='Email registrado previamente')
            ## IF USER HAS NOT BEEN CREATED, CREATE IT
            name=request.form.get('name')
            lastname=request.form.get('lastname')
            password= hashlib.sha256((request.form.get('password')+os.environ.get("SALT_PASSWORD")).encode()).hexdigest()
            query = "INSERT INTO usuarios (name,lastname,email,password) VALUES('"+name+"','"+lastname+"','"+email+"','"+password+"')"
            cursor.execute(query)
            con.commit()#rows = cursor.fetchall()
            close_connection()
            session['user_email']=email
            return redirect(url_for("blog"))
        except Exception as e:
            print(e)
            return jsonify(type='error',msg='Error al registrar usuario!')
    return jsonify(type='error',msg='Error en el Formulario!')

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