# FLASK_APP=server.py FLASK_ENV=development flask run
from flask import Flask, render_template,session,redirect,url_for,request
from application.rutas import blog_api
from flask_wtf import FlaskForm,RecaptchaField
from application.forms import RegisterForm
# from flask_login import login_required, current_user
app = Flask(__name__)
app.config['SECRET_KEY'] = 'grupoC'
app.config['RECAPTCHA_PUBLIC_KEY']='6LfoNwAaAAAAAOKEVTaYDEMvdDfoQTHIKhsU_iIu'
app.config['RECAPTCHA_PRIVATE_KEY']='6LfoNwAaAAAAANd8XtVz4uT5_tTSTuxStL1PXFYV'
app.config['TESTING']=True
app.register_blueprint(blog_api)

@app.route('/')
def home():
    form = RegisterForm(request.form)
    if "user_email" in session:
        return redirect(url_for("blog"))
    else:
        return render_template("home.html", route='home',form=form)

@app.route('/blog')
def blog():
    if "user_email" in session:
        return render_template("blog.html", route='blog',user=session['user_email'])
    else:
        return redirect(url_for("home"))

@app.errorhandler(404)
def not_found(e):
    return redirect(url_for("home"))
