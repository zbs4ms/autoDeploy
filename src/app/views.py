#-*- coding: utf-8 -*-
from flask import render_template
from app import app


@app.route('/')
@app.route('/home')
def home():
    return render_template('homePage.html',title='home')

@app.route('/process/detail/<id>')
def processDetail(id):
    process_name="[Name]"
    return render_template('processDetail.html',title=process_name,process_id=id)

@app.route('/process/edit/<id>')
def processEdit(id):
    process_name="[Name]"
    return render_template('processEdit.html',title=process_name,id=id)

@app.route('/process/new')
def processNew():
    return render_template('processEdit.html',title="")

@app.route('/script/overview')
def scriptOverview():
    return render_template('scriptOverview.html',title="Script Overview")

@app.route('/script/edit/<id>')
def scriptEdit(id):
    print(id)
    return render_template('scriptEdit.html',id=id)

@app.route('/script/create')
def scriptCreate():
    return render_template('scriptEdit.html',title="Script Create")

