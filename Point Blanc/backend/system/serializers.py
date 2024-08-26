from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Drink,Employee
# class model for the authentifacation
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id",'username','password']
        extra_kwargs = {'password':{'write_only':True}}

    # fuction 
    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        return User

# drink serializer
class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model =Drink
        fields=['id', 'name', 'description']

# employee serialization
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=["username","firstName","middleName","surName","phoneNumber","email",
                "ID","Department","DOB","joinedDate","NextofKin","NextofKinNumber"
        ]

        # fuction
        def createemployee(self):
            employee=Employee.objects.create_employee()
            return employee
        