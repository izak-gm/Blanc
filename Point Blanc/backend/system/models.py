from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class for the model
class Drink(models.Model):
    name=models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    

    def __str__(self):
        return self.name+" "+ self.description
# project proposed 
class Employee(models.Model):
    username=models.CharField(max_length=20 ,primary_key=True )
    firstName=models.CharField(max_length=20 )
    middleName=models.CharField(max_length=20 )
    surName=models.CharField(max_length=20 )
    phoneNumber=models.CharField(max_length=20,unique=True)
    email=models.CharField(max_length=50  ,unique=True)
    ID=models.CharField(max_length=20  ,unique=True)
    Department=models.CharField(max_length=20 )
    DOB=models.CharField(max_length=20 )
    joinedDate=models.CharField(max_length=20)
    NextofKin=models.CharField(max_length=200 )
    NextofKinNumber=models.CharField(max_length=20)
    

    # fuction calling the model
    def __str__(self):
        return f'<employee{self.username}>'
