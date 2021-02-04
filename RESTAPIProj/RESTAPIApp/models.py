from django.db import models

# Create your models here.
#This is an employee model for testing the REST API.
class Employee(models.Model):
    """
    This model will store the E_id, E_name, E_mob.
    """
    E_id = models.AutoField(primary_key=True) #employee id
    E_name = models.CharField(max_length=30)  #employee name
    E_mob = models.CharField(max_length=15)  #employee mobile number