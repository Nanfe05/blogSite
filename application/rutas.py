# API ROUTES 
import os
from flask import Flask,Blueprint,jsonify,request, session,redirect,url_for,current_app
from application.forms import LoginForm,RegisterForm,RecoverForm,AddBlogForm,AddCommentForm

from db.db import get_db,close_connection
from werkzeug.security import generate_password_hash,check_password_hash
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired


blog_api=Blueprint('blog_api',__name__)
#app.config('config.cfg')
#mail = Mail(blog_api)





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
                password_real= user_exists[0][4]
                if(check_password_hash(password_real,request.form.get('password'))):
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


               
@blog_api.route('/blog_api/confirm_email/<token>',methods=['GET'] )
def confirm_email(token):
    form = RegisterForm(request.form)
    #email = email
    email=''

    con = get_db()
    cursor = con.cursor()
    query = "UPDATE usuarios SET emailValidated=True WHERE email='"+email+"'"
    cursor.execute(query)
    con.commit()#rows = cursor.fetchall()        
    return '<h1>Confirmacion completa</h1>'
@blog_api.route('/blog_api/confirm_email/<token>/<string:email>',methods=['GET'] )    
def confirm_email1(token,email):
    form = RegisterForm(request.form)
    email = email
    

    con = get_db()
    cursor = con.cursor()
    query = "UPDATE usuarios SET emailValidated=True WHERE email='"+email+"'"
    cursor.execute(query)
    con.commit()#rows = cursor.fetchall()        
    return '<h1>Confirmacion completa</h1>'    

   
@blog_api.route('/api/register',methods=['POST'])

def register():
    def gettingapp ():
        app = Flask(__name__)
        s = URLSafeTimedSerializer('grupoC') 
        with app.app_context():  
            app = Flask(__name__)
            current_app.config.from_pyfile('config.cfg')
            mail = Mail(current_app)
            email = request.form.get('email')                      
            token = s.dumps(email, salt='email-confirm')
            msg = Message('Confirm Email', sender='ffernandezj@uninorte.edu.co', recipients=[email])
            link = url_for('blog_api.confirm_email', token=token,  _external=True)
            msg.body = 'Your link is {}/{}'.format(link,email)
            mail.send(msg)   
              
        return app  
    
    form = RegisterForm(request.form)
    form.validate()
    print(form.errors)
    
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
                return jsonify(type='error',msg='Usuario ya existe')
                #return jsonify(type='success',msg='Email registrado previamente')
            ## IF USER HAS NOT BEEN CREATED, CREATE IT
            name=request.form.get('name')
            lastname=request.form.get('lastname')
            password= generate_password_hash(request.form.get('password'))
            #password1=request.form.get('password1')
            query = "INSERT INTO usuarios (name,lastname,email,password) VALUES('"+name+"','"+lastname+"','"+email+"','"+password+"')"
            cursor.execute(query)
            con.commit()#rows = cursor.fetchall()
            close_connection()
            session['user_email']=email
            gettingapp()
            return redirect(url_for("blog"))
            
        except Exception as e:
            print(e)
            return jsonify(type='error',msg=form.errors)
    return jsonify(type='error',msg=form.errors)

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
        title=request.form.get('title')
        subject=request.form.get('subject')
        content=request.form.get('content')
        try:
            #Get User ID
            con = get_db()
            cursor = con.cursor()
            query = "SELECT id FROM usuarios WHERE email='"+session['user_email']+"'"
            cursor.execute(query)
            user_id = cursor.fetchone()[0]
            #Agregar Blog
            query = "INSERT INTO blogs (owner,subject,title,content,isPublished,isActive,dateCreated,dateModified) VALUES('"+str(user_id)+"','"+subject+"','"+title+"','"+content+"','"+str(1)+"','"+str(1)+"','"+str(datetime.datetime.now())+"','"+str(datetime.datetime.now())+"')"
            cursor.execute(query)
            con.commit()
            close_connection()
            return jsonify(type='success',msg='Blog Agregado exitosamente!')
        except Exception as e:
            print(e)
            return jsonify(type='error',msg='Error agregando el blog')
    return jsonify(type='error',msg='No se puede agregar el blog!')

@blog_api.route('/api/editblog',methods=['POST'])
def edit_blog():
    form = AddBlogForm(request.form)
    if form.validate():
        title=request.form.get('title')
        subject=request.form.get('subject')
        content=request.form.get('content')
        blog_id=request.form.get('id')
        try:
            #Get User ID
            con = get_db()
            cursor = con.cursor()
            #Agregar Blog
            query = "UPDATE blogs SET subject='"+subject+"',title='"+title+"',content='"+content+"',dateModified='"+str(datetime.datetime.now())+"' WHERE id="+blog_id+""
            cursor.execute(query)
            con.commit()
            close_connection()
            return jsonify(type='success',msg='Blog Editado exitosamente!')
        except Exception as e:
            print(e)
            return jsonify(type='error',msg='Error agregando el blog')
    return jsonify(type='error',msg='No se puede agregar el blog!')

@blog_api.route('/api/blogs',methods=['GET'])
def get_blogs():
    con = get_db()
    cursor = con.cursor()
    query = "SELECT * FROM blogs"
    cursor.execute(query)
    blogs = cursor.fetchall()
    close_connection()
    # Sending blogs as an array
    return jsonify(blogs)

@blog_api.route('/api/comments',methods=['GET'])
def get_comments():
    con = get_db()
    cursor = con.cursor()
    query = "SELECT * FROM comments"
    cursor.execute(query)
    comments = cursor.fetchall()
    close_connection()
    # Sending comments as an array
    return jsonify(comments)

@blog_api.route('/api/deleteBlog/<id_blog>',methods=['GET'])
def delete_blog(id_blog):
    try:
        con = get_db()
        cursor = con.cursor()
        query = "DELETE FROM blogs WHERE id='"+id_blog+"'"
        cursor.execute(query)
        con.commit()
        close_connection()
        return jsonify(type='success',msg='Hemos borrado satisfactoriamente el blog!')
    except Exception as e:
        return jsonify(type='error',msg='Error Borrando el blog!')

# Sending comments as an array


@blog_api.route('/api/addcomment',methods=['POST'])
def add_comment():
    form = AddCommentForm(request.form)
    if form.validate():
        id_blog=request.form.get('id')
        comment=request.form.get('comment')
        print(id_blog)
        try:
            #Get User ID
            con = get_db()
            cursor = con.cursor()
            query = "SELECT id FROM usuarios WHERE email='"+session['user_email']+"'"
            cursor.execute(query)
            user_id = cursor.fetchone()[0]
            #Agregar Blog
            query = "INSERT INTO comments (owner,comment,isActive,dateCreated) VALUES('"+str(id_blog)+"','"+comment+"','"+str(1)+"','"+str(datetime.datetime.now())+"')"
            cursor.execute(query)
            con.commit()
            close_connection()
            return jsonify(type='success',msg='comentario Agregado exitosamente!')
        except Exception as e:
            print(e)
            return jsonify(type='error',msg='Error agregando el comentario')
    return jsonify(type='error',msg='No se puede agregar el comentario!')

