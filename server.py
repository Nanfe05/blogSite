# FLASK_APP=server.py FLASK_ENV=development flask run
from flask import Flask, render_template
from application.rutas import blog_api
# from flask_login import login_required, current_user
app = Flask(__name__)
app.config['SECRET_KEY'] = 'grupoC'

app.register_blueprint(blog_api)

@app.route('/')
def home():
    return render_template("home.html", route='home')

@app.route('/blog')
def blog():
    return render_template("blog.html", route='blog')

