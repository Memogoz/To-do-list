from flask import render_template, redirect, url_for, request, flash
from app import app
from app.models import Task
from flask_sqlalchemy import SQLAlchemy


    
@app.route("/")
def login():
    return render_template('login.html')




@app.route("/todo", methods=['POST'])
def todo():
    name = request.form['username']

    #taskList = Task.query.all()  # Consulta todas las tareas de la base de datos

    taskList = [
        {'name':'Tarea 1', 'details':'Lorem epsium bla bla bla', 'date':'10/10/24', 'priority':3, 'status':'in progress'},
        {'name':'Tarea 2', 'details':'Lorem epsium bla bla bla', 'date':'10/10/24', 'priority':3, 'status':'in progress'},
        {'name':'Tarea 3', 'details':'Lorem epsium bla bla bla', 'date':'10/10/24', 'priority':3, 'status':'in progress'}
    ]

    return render_template('todo.html', name=name, tasks=taskList)




@app.route('/add_task', methods=['GET', 'POST'])
def add_task():
    name = request.form['name']
    details = request.form['details']
    date = request.form['date']
    priority = request.form['priority']
    status = request.form['status']
    
    new_task = Task(name, details, date, priority, status)
    #db.session.add(new_task)  # Agregar la nueva tarea a la base de datos
    #db.session.commit()
    flash('Tarea agregada exitosamente!')
    return redirect(url_for('todo'))  # Redirige a la página principal




# Ruta para eliminar una tarea
@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task():
    task_id = request.form['task_id']

    #task = Task.query.get_or_404(task_id)  # Busca la tarea por su ID
    #db.session.delete(task)  # Elimina la tarea de la base de datos
    #db.session.commit()
    flash('Tarea eliminada!')
    return redirect(url_for('todo'))




# Ruta para marcar una tarea como completada
@app.route('/complete/<int:task_id>', methods=['POST'])
def complete_task():
    task_id = request.form['task_id']

    #task = Task.query.get_or_404(task_id)
    #task.completed = True  # Marca la tarea como completada
    #db.session.commit()
    flash('Tarea marcada como completada!')
    return redirect(url_for('todo'))
