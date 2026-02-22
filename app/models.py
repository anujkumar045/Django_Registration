from django.db import models

# Create your models here.
class Employee(models.Model):
    Name=models.CharField(max_length=40)
    Contact=models.BigIntegerField()
    Email=models.EmailField()
    Department=models.CharField(max_length=20)
    Code=models.CharField(max_length=20)
    Image=models.FileField()
    

class Department(models.Model):
    Dep_name = models.CharField(max_length=100)
    Dep_code = models.CharField(max_length=20, unique=True)
    Dep_head = models.CharField(max_length=100)
    Dep_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

