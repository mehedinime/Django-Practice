from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomuserModel(AbstractUser):
            USER_TYPE= [
                      
                ('Principal','Principal'),
                ('Teacher','Teacher'),
                ('Student','Student'),
            ]
            usertype=models.CharField(choices=USER_TYPE, max_length=50, null=True)
            name=models.CharField(max_length=50, null=True)
            def __str__(self):
                       return self.username
              
class teacherModel(models.Model):
            username=models.ForeignKey(CustomuserModel, on_delete=models.CASCADE,null=True)
            name=models.CharField( max_length=50,null=True)
            subjact=models.CharField(max_length=100, null=True)
            phone=models.IntegerField(null=True)
            address=models.TextField(null=True)
            def __str__(self):
                            return self.name
              
class studentModel(models.Model):
            user=models.ForeignKey(CustomuserModel, on_delete=models.CASCADE,null=True)
            name=models.CharField( max_length=50,null=True)
            classname=models.CharField( max_length=50, null=True)
            roll=models.IntegerField(null=True)
            mobile=models.IntegerField(null=True)
            address=models.TextField(null=True)
            def __str__(self):
                                return self.classname
              

class ClassModel(models.Model):
              className = models.CharField(max_length=100, null=True)
              seats = models.IntegerField(null=True)
              def __str__(self):
                            return self.className
              
