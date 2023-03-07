from flask_app import app
from flask import render_template, redirect, request, session
from flask import flash
from flask_app.models.student import Student
import re


#==================Route READ ALL==========================#
@app.route('/student')
def students():
    all_students = Student.get_all()
    return render_template ("/dashboard/showstudents.html", all_students = all_students)

#==================Route READ ONE==========================#
@app.route('/student/<int:student_id>/show')
def show_student(student_id):
    data_dict={'id':student_id}
    this_student = Student.get_by_id(data_dict)
    return render_template ("/dashboard/showonestudent.html", this_student=this_student)

#==================Route INSERT==========================#
@app.route('/student/new')
def new_student():
    # if 'user_id' not in session:
    #     return redirect('/')
    return render_template("/dashboard/addstudent.html")

@app.route('/student/create', methods=['POST'])
def create_student():
    print(request.form)
    Student.create_student(request.form)
    return redirect('/student')


#==================Route INSERT==========================#

# @app.route('/student/create', methods=['POST'])
# def add_student():
#     if not Student.validate_student(request.form):
#         return redirect('/student/new')
#     data = {
#         **request.form,
#         'user_id': session['user_id']
#     }
#     print("-"*20, data, "-"*20)
#     Student.create_student(data)
#     return redirect('/student')

#==================Route EDIT==========================#
@app.route('/student/edit/<int:student_id>', methods=['GET', 'POST'])
def edit_student(student_id):
    if 'user_id' not in session:
        return redirect('/student')
    student=Student.get_by_id({'id':student_id})
    return render_template("/dashboard/modifystudent.html", student=student)

@app.route('/student/update', methods=['POST'])
def update_student():
    print("-"*20,request.form['id'],"-"*20) #juste pour vérifier si l'id yo5rej ou pas vu que 7attineh hidden a7na 
    if not Student.validate_student(request.form):
        return redirect('/student/new')
    Student.update_student(request.form)
    return redirect ('/student')

#==================Route DELETE==========================#
@app.route("/student/<int:student_id>/delete")
def delete_student(student_id):
    data_dict = {'id': student_id}
    Student.delete_student(data_dict)
    return redirect("/student")



