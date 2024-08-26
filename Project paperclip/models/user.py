from db import db

class UserModel(db.Model):
    __table__="users"

    id=db.Column(db.Integer ,primary_key=True)
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
            "id":self.id,
            "username":self.userrname,
            "lastName":self.lastName,
            "phoneNumber":self.phoneNumber,
            "email":self.email,
            "nationalID":self.nationalID,
            "joined_date":self.joined_date,
            "nextofkin":self.nextofkin,
            "location":self.location,

        }