from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user
from flask_app.models import classes_has_students
import re

class Classe:
    
    def __init__(self,data):
        self.id=data["id"]
        self.teacher_id=data["teacher_id"]
        self.level=data["level"]
        self.head=data["head"]
        self.calender=data["calender"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]
        self.students_list=[] # on ajoute cette liste puisque les auteurs ont plusieurs livres

    @classmethod
    def create_classe(cls,data):
        query="""
        INSERT INTO classes (teacher_id,level,head,calender)
        VALUES (%(teacher_id)s,%(level)s,%(head)s,%(calender)s);"""
        return connectToMySQL(DATABASE).query_db(query,data)
    
    #==============Read Queries=================#
                #===Read all======#
    @classmethod
    def get_all(cls): 
        query = """SELECT * FROM classes"""
        results= connectToMySQL(DATABASE).query_db(query)
        all_classes= []
        if results:
            for row in results:
                all_classes.append(cls(row))
            return all_classes
        return []
            #===Read one by id======#
    @classmethod
    def get_by_id(cls, data):
        query = """SELECT * FROM classes WHERE id = %(id)s"""
        result= connectToMySQL(DATABASE).query_db(query,data)
        if len(result)<1:
            return False
        return cls(result[0])
    # @classmethod
    # def get_by_id_student(cls, data):
    #     query = """SELECT * FROM classes 
    #     LEFT JOIN classes_has_students ON classes.id = classes_has_students.classe_id  
    #     WHERE classes.id=%(id)s
    #     """
    #     result= connectToMySQL(DATABASE).query_db(query,data)
    #     students = []
    #     if result:
    #         classe = cls(result[0])
    #         for row in result:
    #             student_data = {
    #                 'id':row['id'],
    #                 'student_id':row['classes_has_students.student_id'],
    #                 'classe_id':row['classes_id'],
    #                 'created_at':row['classes_has_students.created_at'],
    #                 'updated_at':row['classes_has_students.updated']
    #             }
    #             one_classes_has_students=classes_has_students.Classe_has_student(student_data)
    #             students.append(one_classes_has_students)
    #         classe.students_list = students
    #         return classe
    #     return None
    @classmethod
    def update_classe(cls, data):
        query = """UPDATE classes SET teacher_id = %(teacher_id)s,level = %(level)s,
        head = %(head)s,calender = %(calender)s 
        WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)    
    
    @classmethod
    def delete_classe(cls, data):
        query = """DELETE FROM classes WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @staticmethod  
    def validate_classe(data):
        is_valid = True
        if len(data['teacher_id'])<1   :
            is_valid = False
            flash("Invalid ..., must be at least 3 characters!", "teacher_id")
        if len(data['level'])<1 :
            is_valid = False
            flash("level must not be blank", "level")
        if len(data['head'])<2:
            is_valid = False
            flash("head must be at least 3 characters!", "head")
        if len(data['calender'])=="":
            is_valid = False
            flash("You should pick a date", "calender")
        return is_valid


