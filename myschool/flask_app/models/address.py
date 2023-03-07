from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Address:
    def __init__(self, data):
        self.id=data['id']
        self.street=data['street']
        self.city=data['city']
        self.state=data['state']
        self.zip_code=data['zip_code']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']


#!=========================================CRUD Queries================================================#
    #==============Create Queries=================#
    @classmethod
    def create_address(cls, data):
        query = """INSERT INTO addresse (street, city, state, zip_code)
        VALUES (%(street)s, %(city)s, %(state)s, %(zip_code)s )"""
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def get_all(cls):
       
        query = """SELECT * FROM address """
        results= connectToMySQL(DATABASE).query_db(query)
        address=[]
        for row in results:
           address = cls(row)
            
           address.append(address)
        return address

            #===Read one by id======#
    @classmethod
    def get_by_id(cls, data):
        query = """SELECT * FROM address WHERE id = %(id)s"""
        result= connectToMySQL(DATABASE).query_db(query,data)
        if len(result)<1:
            return False
        return cls(result[0])

    @classmethod
    def update(cls, data):
        query = """UPDATE address SET street = %(street)s,city = %(city)s,
        state = %(state)s,zip_code = %(zip_code)s
        WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)    
    
    @classmethod
    def delete(cls, data):
        query = """DELETE FROM address WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)
    #==============Read Queries=================#
                #===Read all======#
    
        


