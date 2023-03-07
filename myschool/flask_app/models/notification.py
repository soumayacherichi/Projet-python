from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user 
import re

class Notification:
    def __init__(self,data):
        self.id=data["id"]
        self.sender_id=data["sender_id"]
        self.receiver_id=data["receiver_id"]
        self.receiver=data["receiver"]
        self.libelle=data["libelle"]
        self.type=data["type"]
        self.description=data["description"]
        self.upload=data["upload"]
        self.is_opened=data["is_opened"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]
        # self.owner = user.User.get_by_id({'id':self.user_id}).first_name 



    @classmethod
    def create_notification(cls,data):
        query="""
        INSERT INTO notifications (sender_id,receiver_id,receiver,libelle,type,description,upload,is_opened)
        VALUES (%(sender_id)s,%(receiver_id)s,%(receiver)s,%(libelle)s,%(type)s,%(description)s,%(upload)s,%(is_opened)s)"""
        return connectToMySQL(DATABASE).query_db(query,data)
    
    #==============Read Queries=================#
                #===Read all======#
    @classmethod
    def get_all(cls):
        query = """SELECT * FROM notifications ;"""
        results= connectToMySQL(DATABASE).query_db(query)
        all_notifications = []
        if results:
            for row in results:
                all_notifications.append(cls(row))
            return all_notifications
        return []
            #===Read one by id======#
    @classmethod
    def get_by_id(cls, data):
        query = """SELECT * FROM notifications WHERE id = %(id)s"""
        result= connectToMySQL(DATABASE).query_db(query,data)
        if len(result)<1:
            return False
        return cls(result[0])

    @classmethod
    def update_notification(cls, data):
        query = """UPDATE notifications SET sender_id = %(sender_id)s,receiver_id = %(receiver_id)s,receiver = %(receiver)s,
        libelle = %(libelle)s,type = %(type)s,description = %(description)s,upload = %(upload)s,is_opened = %(is_opened)s
        WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)    
    
    @classmethod
    def delete_notification(cls, data):
        query = """DELETE FROM notifications WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @staticmethod  
    def validate_notification(data):
        is_valid = True
        if len(data['libelle'])<2:
            is_valid = False
            flash("Invalid ..., must be at least 3 characters!", "libelle")
        if len(data['level'])<2:
            is_valid = False
            flash("level must not be blank", "level")
        if len(data['type'])<2:
            is_valid = False
            flash("head must be at least 3 characters!", "type")
        if data['type']=="dairy commnunication":
            if len(data['student'])==0:
                is_valid = False
                flash("Student must be chosen")
        return is_valid
    