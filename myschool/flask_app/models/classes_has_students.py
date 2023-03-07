from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import student
from flask_app.models import classe
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Classe_has_student:
    def __init__(self, data):
        self.id=data['id']
        self.classe_id=data['classe_id']
        self.student_id=data['student_id']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

#!=========================================CRUD Queries================================================#
    #==============Create Queries=================#
    @classmethod
    def create_classe_has_student(cls, data):
        query = """INSERT INTO classes_has_students (classe_id,student_id)
        VALUES (%(classe_id)s, %(student_id)s)"""
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def get_all(cls):
        query = """SELECT * FROM classes_has_student """
        results= connectToMySQL(DATABASE).query_db(query)
        res=[]
        for row in results:
            adresse = cls(row)
            res.append(adresse)
        return res

            #===Read one by id======#
    @classmethod
    def get_by_id(cls, data):
        query = """SELECT * FROM classes_has_student WHERE id = %(id)s"""
        result= connectToMySQL(DATABASE).query_db(query,data)
        if len(result)<1:
            return False
        return cls(result[0])

    @classmethod
    def update(cls, data):
        query = """UPDATE classes_has_students SET classe_id = %(classe_id)s,student_id = %(student_id)s
        
        WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)    
    
    @classmethod
    def delete(cls, data):
        query = """DELETE FROM classes_has_students WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)
    #==============Read Queries=================#
                #===Read all======#
    
        


