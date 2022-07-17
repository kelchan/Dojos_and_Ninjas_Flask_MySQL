from flask import render_template, request, redirect
from flask_app import app
# from flask_app.models.dojos_model import Dojos
# from flask_app.models.ninjas_model import Ninjas

# @app.route( '/ninja/new' )
# def newNinja():
#     return render_template( 'new_ninja.html', dojos = Dojos.get_all() )

# @app.route( '/ninja/create', methods = [ 'POST' ] )
# def createNinja():
#     print( 'New Ninja:', request.form )
#     newNinja = {
#         "first_name" : request.form[ 'first_name' ],
#         "last_name" : request.form[ 'last_name' ],
#         "age" : int(request.form[ 'ninja_age' ]),
#         "dojo_id" : request.form[ 'dojo_id' ]
#     }
#     Ninjas.create( newNinja )
#     return redirect( '/dojos' )


