from flask import render_template
from app import app


@app.route('/')
@app.route('/home')
def home():
    return render_template('homePage.html',title='home')

@app.route('/process/detail/<id>')
def processDetail(id=None):
    process_name="[Name]"
    return render_template('processDetail.html',title=process_name,process_id=id)

@app.route('/process/edit/<id>')
def processEdit(id=None):
    process_name="[Name]"
    return render_template('processEdit.html',title=process_name,id=id)

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