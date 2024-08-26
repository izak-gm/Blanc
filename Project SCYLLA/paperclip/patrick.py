#pyhonprogram to fetch api from a database and also store the  data
#flask api

import os
import sys
from flask import Flask,request,jsonify,json
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#app config
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:''@localhost/register.db'


db=SQLAlchemy(app)

class users(db.Model):
    
    username=db.Column(db.String(20),primary_key=True ,autoincrement = True)
    lastName=db.Column(db.String(255),nullable=False)
    phoneNumber=db.Column(db.Integer ,nullable=False,unique=True)
    email=db.Column(db.String(255) ,nullable=False,unique=True)
    nationalID=db.Column(db.Integer,nullable=False ,unique=True)
    joined_date=db.Column(db.String(200) ,nullable=False)
    nextofkin=db.Column(db.String(255)  ,nullable=False)
    location=db.Column(db.String(255) ,nullable=False)

    def json_return(self):
        return{
            "username":self.username,
            "lastName":self.lastName,
            "phoneNumber":self.phoneNumber,
            "email":self.email,
            "nationalID":self.nationalID,
            "joined_date":self.joined_date,
            "nextofkin":self.nextofkin,
            "location":self.location,

        }


#adding a new user instance
@app.route("/application/user" ,methods=['POST'])
def process_data():
    request_data=request.get_json()
    new_user={
        "username":request_data["username"],
        "lastName":request_data["lastName"],
        "phoneNumber":request_data["phoneNumber"],
        "email":request_data["email"],
        "nationalID":request_data["nationalID"],
        "joined_date":request_data["joined_date"],
        "nextofkin":request_data["nextofkin"]
        }
    db.session.add(new_user)
    db.session.commit()
    return jsonify(message="User created succesfully"),201

@app.route("/application/user" ,methods=['GET'])
def get_all_users():
    Users=users.query.all()
    User_list=[]
    for user in users:
        user_data={
            "username":request_data["username"],
            "lastName":request_data["lastName"],
            "phoneNumber":request_data["phoneNumber"],
            "email":request_data["email"],
            "nationalID":request_data["nationalID"],
            "joined_date":request_data["joined_date"],
            "nextofkin":request_data["nextofkin"],
            "location":request_data["location"]}
        User_list.append(user_data)
    return jsonify(User_list)

#get one employee
@app.route("/application/user/<string:username>" ,methods=['GET'])
def get_all_user(username):
    Users=users.query.get_or_404(username)
    user_data={
            "username":request_data["username"],
            "lastName":request_data["lastName"],
            "phoneNumber":request_data["phoneNumber"],
            "email":request_data["email"],
            "nationalID":request_data["nationalID"],
            "joined_date":request_data["joined_date"],
            "nextofkin":request_data["nextofkin"],
            "location":request_data["location"]
            }
    return jsonify(user_data)


#update a user
@app.route("/application/user/<string:username>" ,methods=['PUT'])
def update_user(username):
    user=users.query.get_or_404(username)
    data=request.json
    for key,value in data.items():
        setattr(user,key,value)
    db.session.commit()
    return jsonify(message='Employee updated successfully')
#delete a user
@app.route("/application/<string:username>" ,methods=['DELETE'])
def delete_user(username):
    user=users.query.get_or_404(username)
    db.session.delete(username)
    db.session.commit()
    return jsonify(message='User deleted successfully')

if __name__=='__main__':
    app.run(debug=True)