
from django.contrib import admin
from django.urls import path
from myApp.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage, name="homePage"),
    path('regester/', regester, name="regester"),
    path('loginPage/', loginPage, name="loginPage"),
    path('techerdelete/<int:myID>', techerdelete, name="techerdelete"),
    
    
    # addTecher
    path('addTecher/', addTecher, name="addTecher"),
    path('teacherlist/', teacherlist, name="teacherlist"),
]
