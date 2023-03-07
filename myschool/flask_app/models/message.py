from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Message:
    def __init__(self, data):
        self.id=data['id']
        self.sender_id=data['sender_id']
        self.receiver_id=data['receiver_id']
        self.reply_to=data['reply_to']
        self.is_opened=data['is_opened']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']


#!=========================================CRUD Queries================================================#
    #==============Create Queries=================#
    @classmethod
    def create_message(cls, data):
        query = """INSERT INTO messages (sender_id, receiver_id, replay_to, is_opened)
        VALUES (%(sender_id)s, %(receiver_id)s, %(replay_to)s, %(is_opened)s )"""
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def get_all(cls):
       
        query = """SELECT * FROM messages """
        results= connectToMySQL(DATABASE).query_db(query)
        messages=[]
        for row in results:
            message = cls(row)
            
            messages.append(message)
        return messages

            #===Read one by id======#
    @classmethod
    def get_by_id(cls, data):
        query = """SELECT * FROM messages WHERE id = %(id)s"""
        result= connectToMySQL(DATABASE).query_db(query,data)
        if len(result)<1:
            return False
        return cls(result[0])

    @classmethod
    def update(cls, data):
        query = """UPDATE messages SET sender_id = %(sender_id)s,receiver_id = %(receiver_id)s,
        reply_to = %(reply_to)s,is_opened = %(is_opened)s 
        WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)    
    
    @classmethod
    def delete(cls, data):
        query = """DELETE FROM messages WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)
    #==============Read Queries=================#
                #===Read all======#
    

