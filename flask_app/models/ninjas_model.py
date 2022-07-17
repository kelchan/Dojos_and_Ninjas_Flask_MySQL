from flask_app.config.mysqlconnection import connectToMySQL
from server import DATABASE



class Ninjas:
    def __init__( self, data ):
        self.id = data[ 'id' ]
        self.first_name = data[ 'first_name' ]
        self.last_name = data[ 'last_name' ]
        self.age = data[ 'age' ]
        self.created_at = data[ 'created_at' ]
        self.updated_at = data[ 'updated_at' ]
        self.dojo_id = data[ 'dojo_id' ]

    @classmethod
    def get_all( cls, data ):
        query = "SELECT * FROM ninjas WHERE dojo_id = %(id)s;"
        # results = connectToMySQL( DATABASE ).query_db( query, data )
        # print( 'results=', results )
        return connectToMySQL( DATABASE ).query_db( query, data )
    
    @classmethod
    def create( cls, data):
        query = "INSERT INTO ninjas( first_name, last_name, age, dojo_id )"
        query += "VALUES( %(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s );"
        return connectToMySQL( DATABASE ).query_db( query, data )

