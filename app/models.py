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