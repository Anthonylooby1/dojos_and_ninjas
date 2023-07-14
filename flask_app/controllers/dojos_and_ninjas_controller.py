from flask import Flask, render_template, request, redirect,session
from flask_app import app
from flask_app.models.ninjas_model import Ninja
from flask_app.models.dojos_and_ninjas_models import Dojo


@app.route('/dojos')
def all_dojos():
    all_dojos = Dojo.get_all_dojo()
    print(all_dojos)
    return render_template('index.html', all_dojos=all_dojos)

@app.route('/dojos', methods=['POST'])
def create_dojo():
    Dojo.create_dojo(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:id>/show')
def show_dojo(id):
    data = {
        'id': id
    }
    one_dojo = Dojo.get_one_with_ninjas(data)
    return render_template('dojo_show.html', one_dojo=one_dojo)



