from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.notification import Notification

#==================Route READ ALL==========================#
@app.route('/notifications')
def notif():
    all_notifications = Notification.get_all()
    print("-+-"*20,all_notifications,"-+-"*20)
    return render_template ("/dashboard/shownotif.html", all_notifications = all_notifications)

@app.route('/notifications_parent')
def notifparent():
    all_notifications_parent = Notification.get_all()
    print("-+-"*20,all_notifications_parent,"-+-"*20)
    return render_template ("/site/notification.html", all_notifications_parent = all_notifications_parent)

@app.route('/dairy')
def dairy_parent():
    all_notifications_parent = Notification.get_all()
    print("-+-"*20,all_notifications_parent,"-+-"*20)
    return render_template("/site/dairy.html", all_notifications_parent = all_notifications_parent )

@app.route('/library')
def library ():
    return render_template('site/library.html')

@app.route('/gallery')
def gallery ():
    return render_template('site/gallery.html')

@app.route('/publication')
def publication ():
    return render_template('site/publication.html')

@app.route('/schedule')
def schedule ():
    return render_template('site/schedule.html')

#==================Route INSERT==========================#

@app.route('/notifications/new')
def new_notif():
    # if 'user_id' not in session:
    #     return redirect('/')
    return render_template('/dashboard/addnotif.html')

@app.route('/notification/create', methods=['POST'])
def add_notification():
    if not Notification.validate_notification(request.form):
        return redirect('notifications/new')
    data = {
        **request.form,
        'user_id': session['user_id']
    }
    print("-"*20, data, "-"*20)
    Notification.create_notification(data)
    return redirect('/notification')

#==================Route EDIT==========================#
@app.route('/notification/edit/<int:notification_id>', methods=['GET', 'POST'])
def edit_notification(notification_id):
    if 'user_id' not in session:
        return redirect('/notification')
    notification=Notification.get_by_id({'id':notification_id})
    return render_template("/dashboard/modifynotif.html", notification=notification)

@app.route('/notification/update', methods=['POST'])
def update_notification():
    print("-"*20,request.form['id'],"-"*20) #juste pour vérifier si l'id yo5rej ou pas vu que 7attineh hidden a7na 
    if not Notification.validate_notification(request.form):
        return redirect('/notification/new')
    Notification.update_notification(request.form)
    return redirect ('/notification')

#==================Route DELETE==========================#
@app.route("/notification/<int:notification_id>/delete")
def delete_notification(notification_id):
    data_dict = {'id': notification_id}
    Notification.delete_notification(data_dict)
    return redirect("/notification")



