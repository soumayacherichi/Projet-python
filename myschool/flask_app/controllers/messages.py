from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.course import Course
from flask_app.models.user import User

@app.route('/message')
def message ():
    return render_template('site/messagerie.html')