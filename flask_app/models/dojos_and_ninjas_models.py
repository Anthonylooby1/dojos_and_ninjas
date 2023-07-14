from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninjas_model import Ninja
DATABASE = 'dojos_and_ninjas'

class Dojo:
    def __init__(self,data) -> None:
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all_dojo(cls):
        query = """
            SELECT * FROM dojos
        """    
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        all_dojos = []
        for row_from_db in results:
            dojo_instance = cls(row_from_db)
            all_dojos.append(dojo_instance)
        return all_dojos
    
    @classmethod
    def create_dojo(cls,data):
        query = """
            INSERT INTO dojos (name)
            VALUES (%(name)s)
        """
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod 
    def get_one_with_ninjas(cls,data):
        query = """
            SELECT * FROM dojos JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query,data)
        print(results)
        if not results:
            return False
        
        dojo = cls(results[0])

        for row in results:
            ninja_data = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at'],
                'dojo_id': row['dojo_id']
            }
            ninja = Ninja(ninja_data)
            dojo.ninjas.append(ninja)
        
        return dojo
    

