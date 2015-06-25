#-*- coding: utf-8 -*-
from flask import render_template
from app import app


@app.route('/')
@app.route('/home')
def home():
    return render_template('homePage.html',title='home')

@app.route('/process/detail/<id>')
def processDetail(id):
    return render_template('processDetail.html',process_id=id)

@app.route('/process/edit/<id>')
def processEdit(id):
    return render_template('processEdit.html',process_id=id)

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

@app.route('/task/create/<process_id>')
def taskCreate(process_id):
    return render_template('createTask.html',process_id=process_id)

@app.route('/task/config/<task_id>')
def taskConfig(task_id):
    print task_id
    return render_template('taskConfig.html',task_id=task_id)

@app.route('/task/execute/<task_id>')
def taskExecute(task_id):
    print task_id
    isDone=0
    return render_template('executePage.html',task_id=task_id,isDone=isDone)


