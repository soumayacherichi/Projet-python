from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import address
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self, data):
        self.id=data['id']
        self.address_id=data['address_id']
        self.status=data['status']
        self.login_in=data['login_in']
        self.login_out=data['login_out']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.tel=data['tel']
        self.password=data['password']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.address=address.Address.get_by_id({'id':self.address_id}).state



#!=========================================CRUD Queries================================================#
    #=================Create Queries=====================#
    @classmethod
    def create_user(cls, data):
        query = """INSERT INTO users (adresse_id, status, first_name, last_name, email,tel, password)
        VALUES (%(adresse_id)s, %(status)s, %(first_name)s, %(last_name)s, %(email)s,%(tel)s, %(password)s )"""
        return connectToMySQL(DATABASE).query_db(query,data)
    
    #==================View all users=====================#
    @classmethod
    def get_all(cls):
       
        query = """SELECT * FROM users"""
        results= connectToMySQL(DATABASE).query_db(query)
        users=[]
        for row in results:
            user = cls(row)
            users.append(user)
        return users
    #==================USER + ADDRESS=====================#

    @classmethod
    def get_one(cls,data_dict):
        query = """SELECT * FROM users JOIN address ON users.address_id = address.address_id  WHERE users.id=%(id)s ;"""
        result = connectToMySQL(DATABASE).query_db(query,data_dict)
        address = []
        if result:
            this_user =  cls(result[0])
            for row in result:
                address_data = {
                    'id':row['address.id'],
                    'street':row['street'],
                    'city': row['city'],
                    'state': row['state'],
                    'zip_code': row['zip_code'],
                    'created_at' :row['address.created_at'],
                    'updated_at' :row['address.updated_at']
                }
                one_address = address.Address(address_data)
                address.append(one_address)
                this_user.address_list = address
            return this_user
        return None
    #==============View all teachers=================#
    @classmethod
    def get_all_teacher(cls):
       
        query = """SELECT * FROM users where status=1 ;"""
        results= connectToMySQL(DATABASE).query_db(query)
        users=[]
        for row in results:
            user = cls(row)
            users.append(user)
        return users
    #==============View all parents=================#
    @classmethod
    def get_all_parent(cls):
       
        query = """SELECT * FROM users where status=2"""
        results= connectToMySQL(DATABASE).query_db(query)
        users=[]
        for row in results:
            user = cls(row)
            users.append(user)
        return users
    
    #=======================Read one by id====================#
    @classmethod
    def get_by_id(cls, data):
        query = """SELECT * FROM users WHERE id = %(id)s"""
        result= connectToMySQL(DATABASE).query_db(query,data)
        if len(result)<1:
            return False
        return cls(result[0])
    
    #=====================Read one by email======================#
    @classmethod
    def get_by_email(cls, data):
        query = """SELECT * FROM users WHERE email = %(email)s"""
        result= connectToMySQL(DATABASE).query_db(query,data)
        if len(result)<1:
            return False
        return result
    
    #=====================Update======================#
    @classmethod
    def update_user(cls, data):
        query = """UPDATE users SET address_id = %(address_id)s,status = %(status)s,
        login_in = %(login_in)s,login_out = %(login_out)s,first_name = %(first_name)s,last_name = %(last_name)s,email = %(email)s,tel = %(tel)s,password = %(password)s,tel = %(tel)s 
        WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)    
    
    #=====================Delete======================#
    @classmethod
    def delete_user(cls, data):
        query = """DELETE FROM users WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)
    

    @staticmethod  
    def validate_user(data):
        is_valid = True
        if len(data['first_name'])<2:
            is_valid = False
            flash("Invalid first name, must be greater than 2 characters!", "reg")
        if len(data['last_name'])<2:
            is_valid = False
            flash("Invalid last name, must be greater than 2 characters!", "reg")
        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!", "reg")
            is_valid = False
        elif User.get_by_email({'email': data['email']}):
            is_valid = False
            flash("email address already exists!", "email")
        elif len(data['tel'])<8:
            is_valid = False
            flash("Invalid tel, must be greater than 8 characters!", "reg")
        # if len(data['password'])<4:
        #     is_valid = False
        #     flash("Invalid password, must be greater than 8 characters!", "reg")
        # elif data['password']!=data['confirm_password']:
        #     flash("Password and confirm_password must match!", "reg")
        #     is_valid = False
        return is_valid


