from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models import address
from flask_app.models.user import User


#==================Route Dashboard admin==========================#
@app.route('/')
def user():
    return render_template('dashboard/admin_dashboard.html')

#==================Route Dashboard teacher==========================#

@app.route('/teacherdash')
def teacher():
    return render_template('dashboard/teacher_dashboard.html')

#==================Other Routes admin==========================#

@app.route('/calender')
def calender():
    return render_template('dashboard/showcalendars.html')

#==================Other Routes parent==========================#
@app.route('/home')
def home ():
    return render_template('site/landing-page.html')

@app.route('/about')
def about ():
    return render_template('site/about.html')

@app.route('/aboutuser')
def aboutuser ():
    return render_template('site/aboutuser.html')

@app.route('/access')
def access ():
    return render_template('site/index.html')

@app.route('/profile')
def profile ():
    return render_template('site/profile.html')

@app.route('/editinfo')
def info ():
    return render_template('site/editinfo.html')
@app.route('/editaddress')
def adr ():
    return render_template('site/editadress.html')

@app.route('/typenotif')
def type ():
    return render_template('site/typenotif.html')

@app.route('/editpwd')
def pswd ():
    return render_template('site/password.html')

@app.route('/contact')
def contact ():
    return render_template('site/contacts.html')

@app.route('/user/logout')
def log ():
    return render_template('site/login.html')

#==================READ ALL ==========================#
@app.route('/user/login',methods=['POST'])
def login():
    user_from_db= User.get_by_email(request.form)
    if not user_from_db:
        flash("invalid email address/password", "email")
        return redirect('/')
    # if not bcrypt.check_password_hash(user_from_db.password, request.form['password']):
    #     flash("Invalid Email/Password", "email")
    #     return redirect('/')
    session['user_id']=user_from_db.id
    return redirect('/access')

@app.route('/teacher')
def all_teachers():
    all_teachers = User.get_all_teacher()
    return render_template ("/dashboard/show_teacher.html", all_teachers = all_teachers)

@app.route('/parent')
def all_parents():
    all_parents = User.get_all_parent()
    return render_template ("/dashboard/showparents.html", all_parents = all_parents)

#==================Route READ ONE==========================#
@app.route('/parent/<int:parent_id>/show')
def show_parent(parent_id):
    data_dict={'id':parent_id}
    this_parent = User.get_by_id(data_dict)
    return render_template ("/dashboard/showoneparent.html", this_parent=this_parent)

@app.route('/teacher/<int:teacher_id>/show')
def show_teacher(teacher_id):
    data_dict={'id':teacher_id}
    this_teacher = User.get_by_id(data_dict)
    return render_template ("/dashboard/showoneteacher.html", this_teacher=this_teacher)


#==================INSERT ==========================#

@app.route('/parent/new')
def new_parent():
    # if 'user_id' not in session:
    #     return redirect('/')
    return render_template("/dashboard/addparent.html")

@app.route('/parent/create', methods=['POST'])
def create_parent():
    print(request.form)
    User.create_user(request.form)
    return redirect('/parent')

@app.route('/teacher/new')
def new_teacher():
    # if 'user_id' not in session:
    #     return redirect('/')
    return render_template("/dashboard/add_teacher.html")

@app.route('/teacher/create', methods=['POST'])
def create_teacher():
    print(request.form)
    User.create_user(request.form)
    return redirect('/teacher')





# @app.route('/user/register', methods=['POST'])
# def register():
#     if User.validate_user(request.form):
#         # print("-"*20,request.form ['password'],"-"*20)
#         # hashed_password = bcrypt.generate_password_hash(request.form['password'])
#         # print("*"*20,hashed_password,"*"*20)
#         data = {
#             'full_name': request.form['full_name'],
#             'phone': request.form['phone'],
#             'email': request.form['email'],
#             'password': request.form['password'],
#         }
#         user_id= User.create_user(data)
#         print("-"*20,user_id,"-"*20)
#         session['user_id']= user_id
#         return redirect('/')
#     return redirect('/')

# @app.route('/dashboard')
# def dashboard():
#     logged_user = User.get_by_id({'id':session['user_id']})
#     all_shows =Show.get_all()
#     return render_template("dashboard.html",logged_user=logged_user, all_shows=all_shows)

# @app.route('/user/login',methods=['POST'])
# def login():
#     user_from_db= User.get_by_email(request.form)
#     if not user_from_db:
#         flash("invalid email address/password", "email")
#         return redirect('/')
#     # if not bcrypt.check_password_hash(user_from_db.password, request.form['password']):
#     #     flash("Invalid Email/Password", "email")
#         # return redirect('/')
#     session['user_id']=user_from_db.id
#     return redirect('/')
    
# @app.route('/user/logout')
# def logout():
#     session.clear()
#     return render_template('site/login.html')

# @app.route('/shows/like/<int:show_id>')
# def like_show(show_id):
#     if 'user_id' not in session:
#         return redirect('/')
#     User.like_show({'user_id':session['user_id'],'show_id':show_id})
#     return redirect('/dashboard')

# @app.route('/shows/unlike/<int:show_id>')
# def unlike_show(show_id):
#     if 'user_id' not in session:
#         return redirect('/')
#     User.unlike_show(show_id)
#     return redirect('/dashboard')