from flask import render_template, flash, redirect
from app import app


@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',title='Home',user=user,posts=posts)


@app.route('/')
@app.route('/home')
def home():
    return render_template('homePage.html',title='home')

@app.route('/process/detail/<name>')
def processDetail(name=None):
    return render_template('processDetail.html',title=name)

@app.route('/process/edit/<name>')
def processEdit(name=None):

    return render_template('processEdit.html',title=name)

@app.route('/process/new')
def processNew():
    return render_template('processEdit.html',title="")

@app.route('/script/overview')
def scriptOverview():
    return render_template('scriptOverview.html',title="Script Overview")

@app.route('/script/edit/<id>')
def scriptEdit(id=None):
    name=id
    return render_template('scriptDetail.html',title=name)

@app.route('/script/create')
def scriptCreate():
    return render_template('scriptDetail.html',title="Script Create")