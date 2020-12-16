# FLASK_APP=server.py FLASK_ENV=development flask run
from flask import Flask, render_template,session,redirect,url_for
from application.rutas import blog_api
# from flask_login import login_required, current_user
app = Flask(__name__)
app.config['SECRET_KEY'] = 'grupoC'

app.register_blueprint(blog_api)

@app.route('/')
def home():
    if "user_email" in session:
        return redirect(url_for("blog"))
    else:
        return render_template("home.html", route='home')

@app.route('/blog')
def blog():
    if "user_email" in session:
        return render_template("blog.html", route='blog',user=session['user_email'])
    else:
        return redirect(url_for("home"))

@app.errorhandler(404)
def not_found(e):
    return redirect(url_for("home"))