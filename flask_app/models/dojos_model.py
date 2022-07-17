from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models.ninjas_model import Ninjas

class Dojos:
    def __init__(self, data):
        self.id = data[ 'id' ]
        self.name = data[ 'name' ]
        self.created_at = data[ 'created_at' ]
        self.updated_at = data[ 'updated_at' ]

    @classmethod
    def get_all( cls ):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL( DATABASE ).query_db( query )
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    @classmethod
    def create( cls, data ):
        query = "INSERT INTO dojos( name )"
        query += "VALUES( %(name)s );"
        return connectToMySQL( DATABASE ).query_db( query, data )

    @classmethod
    def get_one( cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        return connectToMySQL( DATABASE ).query_db( query, data )



