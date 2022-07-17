from flask_app.controllers import dojos_controller, ninjas_controller
from flask_app import app

DATABASE = 'dojos_and_ninjas_schema'





if __name__=="__main__":
    app.run(debug=True)