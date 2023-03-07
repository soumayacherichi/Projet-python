from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Student:
    def __init__(self, data):
        self.id=data['id']
        self.parent_id=data['parent_id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.birthadate=data['birthadate']
        self.gender=data['gender']
        self.inscription=data['inscription']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']


#!=========================================CRUD Queries================================================#
    #==============Create Queries=================#
    @classmethod
    def create_student(cls, data):
        query = """INSERT INTO students (parent_id, first_name, last_name, birthadate, gender, inscription)
        VALUES (%(parent_id)s, %(first_name)s, %(last_name)s, %(birthadate)s, %(gender)s , %(inscription)s)"""
        return connectToMySQL(DATABASE).query_db(query,data)
    
    #=====================READ ALL======================#
    @classmethod
    def get_all(cls):
        query = """SELECT * FROM students"""
        results= connectToMySQL(DATABASE).query_db(query)
        all_students=[]
        if results:
            for row in results:
                all_students.append(cls(row)) 
            return all_students
        return []
    #=====================READ ONE======================#
    @classmethod
    def get_by_id(cls, data):
        query = """SELECT * FROM students WHERE id = %(id)s"""
        result= connectToMySQL(DATABASE).query_db(query,data)
        if len(result)<1:
            return False
        return cls(result[0])

        #=====================Update======================#
    @classmethod
    def update(cls, data):
        query = """UPDATE students SET parent_id = %(parent_id)s,first_name = %(first_name)s,
        last_name = %(last_name)s,birthadate = %(birthadate)s,gender = %(gender)s,inscription = %(inscription)s 
        WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)    
    
        #=====================Delete======================#
    @classmethod
    def delete(cls, data):
        query = """DELETE FROM students WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)
    #==============Read Queries=================#
                #===Read all======#
   
    @staticmethod  
    def validate_student(data):
        is_valid = True
        if len(data['first_name'])<2:
            is_valid = False
            flash("Invalid first name, must be greater than 2 characters!", "reg")
        if len(data['last_name'])<2:
            is_valid = False
        elif len(data['birthaday'])==0:
            is_valid = False
            flash("Invalid birthday, must be greater than 8 characters!", "reg")
        # if len(data['password'])<4:
        #     is_valid = False
        #     flash("Invalid password, must be greater than 8 characters!", "reg")
        # elif data['password']!=data['confirm_password']:
        #     flash("Password and confirm_password must match!", "reg")
        #     is_valid = False
        return is_valid


