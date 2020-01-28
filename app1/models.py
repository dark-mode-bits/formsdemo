from django.db import models

# Create your models here.
class EmployeeModel(models.Model):
    name =models.CharField(max_length=20)
    age = models.IntegerField()
    contact_no = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=10)
    re_password = models.CharField(max_length=10)