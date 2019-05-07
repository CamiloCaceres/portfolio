from flask import Flask, request, render_template, flash
from app import app
from app import props as properties

@app.route('/')
def base(): 
    props = properties.main['proyectos']
    return render_template('index.html', props=props)