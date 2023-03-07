from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.classe import Classe
from flask_app.models.user import User

#==================Route READ ALL==========================#
@app.route('/classe')
def classes():
    all_classes = Classe.get_all()
    return render_template ("/dashboard/showclasses.html", all_classes = all_classes)

#==================Route READ ONE==========================#
@app.route('/classe/<int:classe_id>/show')
def show_classe(classe_id):
    data_dict={'id':classe_id}
    this_classe = Classe.get_by_id(data_dict)
    return render_template ("/dashboard/showoneclasse.html", this_classe=this_classe)

#==================Route INSERT==========================#
@app.route('/classe/new')
def classe():
    # if 'user_id' not in session:
    #     return redirect('/classe')
    return render_template('/dashboard/addclass.html')

@app.route('/classe/create', methods=['POST'])
def add_classe():
    print(request.form,"+"*25)
    if Classe.validate_classe(request.form):
        print(request.form,"+"*25)
        Classe.create_classe(request.form)
        return redirect('/classe')
    return render_template('/dashboard/addclass.html')

#==================Route EDIT==========================#
@app.route('/classe/edit/<int:classe_id>', methods=['GET', 'POST'])
def edit_classe(classe_id):
    # if 'user_id' not in session:
    #     return redirect('/classe')
    classe=Classe.get_by_id({'id':classe_id})
    return render_template("/dashboard/modifyclass.html", classe=classe)

@app.route('/classe/update', methods=['POST'])
def update_classe():
    print("-"*20,request.form['id'],"-"*20) #juste pour vérifier si l'id yo5rej ou pas vu que 7attineh hidden a7na 
    if not Classe.validate_classe(request.form):
        return redirect('/classe/new')
    Classe.update_classe(request.form)
    return redirect ('/classe')

#==================Route DELETE==========================#
@app.route("/classe/<int:classe_id>/delete")
def delete_classe(classe_id):
    data_dict = {'id': classe_id}
    Classe.delete_classe(data_dict)
    return redirect("/classe")

