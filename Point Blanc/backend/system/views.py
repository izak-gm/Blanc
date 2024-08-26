from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics,status
from .serializers import UserSerializer,DrinkSerializer,EmployeeSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.http import JsonResponse
from .models import Drink,Employee
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
# user class from the serializers
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class= UserSerializer
    permission_classes = [AllowAny]

# views endpoints
@api_view(['GET','POST'])
def drink_list(request):
    if request.method=='GET':
        drinks = Drink.objects.all()
        drinkserializer = DrinkSerializer(drinks,many=True)
        return JsonResponse({"drinks":drinkserializer.data},safe=False)
    if request.method=='POST':
        drinksserializer=DrinkSerializer(data=request.data)
        if drinksserializer.is_valid():
            drinksserializer.save()
            return Response(drinksserializer.data,status=status.HTTP_201_CREATED)


# employee deatails
@api_view(['GET',"POST"])
def employee_details(request):
    if request.method=="GET":
        employees=Employee.objects.all()
        employeesSerializer=EmployeeSerializer(employees, many=True)
        return JsonResponse({"employees":employeesSerializer.data},safe=False)
    elif request.method=="POST":
        employeesSerializer=EmployeeSerializer(data=request.data)
        if employeesSerializer.is_valid():
            employeesSerializer.save()
            return JsonResponse(employeesSerializer.data ,status=HTTP_201_CREATED)
        return JsonResponse(employeesSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'POST'])
# def employee_details(request):
#     if request.method == 'GET':
#         employees = Employee.objects.all()
#         employees_serializer = EmployeeSerializer(employees, many=True)
#         return JsonResponse({"employees": employees_serializer.data}, safe=False)

#     elif request.method == 'POST':
#         employees_serializer = EmployeeSerializer(data=request.data)
#         if employees_serializer.is_valid():
#             employees_serializer.save()
#             return JsonResponse(employees_serializer.data, status=status.HTTP_201_CREATED)
#         return JsonResponse(employees_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# @api_view(['POST'])
# def add_employee():
#     # Get JSON data from request
#     data = request.get_json()

#     # Extract details
#     name = data.get('name')
#     age = data.get('age')
#     position = data.get('position')
#     salary = data.get('salary')

#     # Create a new employee dictionary
#     new_employee = {
#         'id': len(employees) + 1,  # Simple ID generation
#         'name': name,
#         'age': age,
#         'position': position,
#         'salary': salary
#     }

#     # Add the new employee to the list
#     employees.append(new_employee)

#     return jsonify({'message': 'Employee added successfully', 'employee': new_employee}), 201
