from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Mark:
    def __init__(self, data):
        self.id=data['id']
        self.student_id=data['student_id']
        self.course_id=data['course_id']
        self.note=data['note']
        self.observation=data['observation']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

#!=========================================CRUD Queries================================================#
    #==============Create Queries=================#
    @classmethod
    def create_mark(cls, data):
        query = """INSERT INTO marks (student_id, course_id, note, observation)
        VALUES (%(student_id)s, %(course_id)s, %(note)s, %(observation)s )"""
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def get_all(cls):
       
        query = """SELECT * FROM marks """
        results= connectToMySQL(DATABASE).query_db(query)
        marks=[]
        for row in results:
            mark = cls(row)
            
            marks.append(mark)
        return marks

            #===Read one by id======#
    @classmethod
    def get_by_id(cls, data):
        query = """SELECT * FROM marks WHERE id = %(id)s"""
        result= connectToMySQL(DATABASE).query_db(query,data)
        if len(result)<1:
            return False
        return cls(result[0])

    @classmethod
    def update(cls, data):
        query = """UPDATE marks SET student_id = %(student_id)s,course_id = %(course_id)s,
        note = %(note)s,observation = %(observation)s
        WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)    
    
    @classmethod
    def delete(cls, data):
        query = """DELETE FROM marks WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)
    #==============Read Queries=================#
                #===Read all======#
    
        


