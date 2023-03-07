from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Course:
    def __init__(self, data):
        self.id=data['id']
        self.classe_id=data['classe_id']
        self.libelle=data['libelle']
        self.description=data['description']
        self.type=data['type']
        self.upload=data['upload']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']


#!=========================================CRUD Queries================================================#
    #==============Create Queries=================#
    @classmethod
    def create_course(cls, data):
        query = """INSERT INTO courses (classe_id, libelle, description, type, upload)
        VALUES (%(classe_id)s,%(libelle)s, %(description)s, %(type)s, %(upload)s )"""
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def get_all(cls):
       
        query = """SELECT * FROM courses """
        results= connectToMySQL(DATABASE).query_db(query)
        courses=[]
        for row in results:
          course = cls(row)
            
          courses.append(course)
        return courses

            #===Read one by id======#
    @classmethod
    def get_by_id(cls, data):
        query = """SELECT * FROM courses WHERE id = %(id)s"""
        result= connectToMySQL(DATABASE).query_db(query,data)
        if len(result)<1:
            return False
        return cls(result[0])

    @classmethod
    def update(cls, data):
        query = """UPDATE courses SET classe_id = %(classe_id)s libelle = %(libelle)s,description = %(description)s,
        type = %(type)s,upload = %(upload)s
        WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)    
    
    @classmethod
    def delete(cls, data):
        query = """DELETE FROM courses WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)
    #==============Read Queries=================#
                #===Read all======#
    
        


