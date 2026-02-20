from django.db import models

# Create your models here.
class Employee(models.Model):
    Name=models.CharField(max_length=40)
    Gender=models.CharField(max_length=20)
    Qualification=models.CharField(max_length=20)
    Age_group=models.CharField(max_length=10)
    Email=models.EmailField()
    Contact=models.BigIntegerField()
    Password=models.CharField(max_length=8)
    Confirm_Password=models.CharField(max_length=8,null=True)

class Department(models.Model):
    Dep_name = models.CharField(max_length=100)
    Dep_code = models.CharField(max_length=20, unique=True)
    Dep_head = models.CharField(max_length=100)
    Dep_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

