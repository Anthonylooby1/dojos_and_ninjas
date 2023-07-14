from flask import Flask, render_template, request, redirect,session
from flask_app import app
from flask_app.models.dojos_and_ninjas_models import Dojo
from flask_app.models.ninjas_model import Ninja

@app.route('/ninjas/new')
def new_ninja():
    all_dojos = Dojo.get_all_dojo()
    return render_template("ninjas_new.html", all_dojos=all_dojos)

@app.route('/ninjas/create', methods=['POST'])
def create_ninja():
    print("request form", request.form)
    Ninja.create_ninja(request.form)
    return redirect(f'/dojos/{request.form["dojo_id"]}/show')



