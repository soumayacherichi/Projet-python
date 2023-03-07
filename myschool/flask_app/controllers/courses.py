from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.course import Course
from flask_app.models.user import User

#==================Route READ ALL==========================#
@app.route('/course')
def courses():
    all_courses = Course.get_all()
    return render_template ("/dashboard/showcourses.html", all_courses = all_courses)

#==================Route READ ONE==========================#
@app.route('/course/<int:course_id>/show')
def show_course(course_id):
    data_dict={'id':course_id}
    this_course = Course.get_by_id(data_dict)
    return render_template ("/dashboard/showonecourse.html", this_course=this_course)

#==================Route INSERT==========================#
@app.route('/course/new')
def course():
    # if 'user_id' not in session:
    #     return redirect('/course')
    return render_template('/dashboard/addcourses.html')

@app.route('/course/create', methods=['POST'])
def add_course():
    if not Course.validate_course(request.form):
        return redirect('/course/new')
    data = {
        **request.form,
        'user_id': session['user_id']
    }
    print("-"*20, data, "-"*20)
    Course.create_course(data)
    return redirect('/course')

#==================Route EDIT==========================#
@app.route('/course/edit/<int:course_id>', methods=['GET', 'POST'])
def edit_course(course_id):
    if 'user_id' not in session:
        return redirect('/course')
    course=Course.get_by_id({'id':course_id})
    return render_template("/dashboard/modifycourse.html", course=course)

@app.route('/course/update', methods=['POST'])
def update_course():
    print("-"*20,request.form['id'],"-"*20) #juste pour vérifier si l'id yo5rej ou pas vu que 7attineh hidden a7na 
    if not Course.validate_course(request.form):
        return redirect('/course/new')
    Course.update_course(request.form)
    return redirect ('/course')

#==================Route DELETE==========================#
@app.route("/course/<int:course_id>/delete")
def delete_course(course_id):
    data_dict = {'id': course_id}
    Course.delete_course(data_dict)
    return redirect("/course")

