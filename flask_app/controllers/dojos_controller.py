from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.dojos_model import Dojos
from flask_app.models.ninjas_model import Ninjas

@app.route( '/' )
def index():
    return redirect( '/dojos' )

@app.route( '/dojos' )
def dojos():
    return render_template( 'dojo.html', dojos = Dojos.get_all() )

@app.route( '/dojo/create', methods = ['POST'] )
def create_dojo():
    new_dojo = {
        "name" : request.form['name']
    }
    Dojos.create( new_dojo )
    return redirect( '/dojos' )

@app.route( '/dojos/<int:id>' )
def display_dojo( id ):
    data = {
        "id" : id
    }
    current_dojo = Dojos.get_one( data )
    current_ninjas = Ninjas.get_all( data )
    print( 'current_ninjas =======', current_ninjas)
    return render_template( "dojo_show.html", current_dojo = current_dojo, current_ninjas = current_ninjas )




@app.route( '/ninja/new' )
def newNinja():
    return render_template( 'new_ninja.html', dojos = Dojos.get_all() )

@app.route( '/ninja/create', methods = [ 'POST' ] )
def createNinja():
    newNinja = {
        "first_name" : request.form[ 'first_name' ],
        "last_name" : request.form[ 'last_name' ],
        "age" : int(request.form[ 'age' ]),
        "dojo_id" : request.form[ 'dojo_id' ]
    }
    print( 'New Ninja:', request.form )
    Ninjas.create( newNinja )
    return redirect( '/dojos' )

