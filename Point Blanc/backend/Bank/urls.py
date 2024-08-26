"""
URL configuration for Bank project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from system.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from system import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # url paths createuserview tobe called
    path('system/user/register/' ,CreateUserView.as_view() ,name ='register'),
    path('system/token/' ,TokenObtainPairView.as_view() ,name='get_token'),
    path('system/token/refresh/' ,TokenRefreshView.as_view(), name='refesh'),
    path('system-auth/' , include('rest_framework.urls')),
    path('system/user/register/drinks/' ,views.drink_list),
    path('employee/',views.employee_details , name='employee')
]
