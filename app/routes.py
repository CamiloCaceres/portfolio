from flask import Flask, request, render_template, flash
from app import app
from app import props 

@app.route('/')
def base(): 
    projects = props.main['proyectos']
    skills = props.main['skills']

    return render_template('index.html', projects=projects, skills=skills)