# from _typeshed import NoneType
from django.db import models

# Create your models here.
#This is an employee model for testing the REST API.
class PropertyList(models.Model):
    """
    This model will store the information about all the properties with their description and other information and we will use this model in general search.
    """
    Prop_ID = models.AutoField(primary_key=True)

    PropertyName = models.CharField(max_length=60)
    
    Proprety_Image = models.ImageField(upload_to = 'static/Property_images')
    
    Property_Price = models.CharField(max_length=10)
    
    Property_Description = models.TextField(max_length=180)
    
    PropertyStat = [
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed'),
        ('Ready to move', 'Ready to move'),
    ]
    PropertyStatus = models.CharField(max_length=20, choices=PropertyStat)
    
    PropertyType = [
        ('Residential', 'Residentail'),
        ('Commercial', 'Commercial'),
    ]
    Property_Type = models.CharField(max_length=20, choices=PropertyType, default='Residential')

    BuilderName = models.CharField(max_length=30)
    
    MultipleLocations = [
        ('Bangalore', 'Bangalore'),
        ('Mumbai', 'Mumbai'),
        ('Delhi', 'Delhi'),
        ('Punjab', 'Punjab'),
    ]
    Location = models.CharField(max_length=20, choices=MultipleLocations)
    
    PropertyAddress = models.CharField(max_length=100)
    
    Area_in_sqft = models.CharField(max_length=20)
    
    BHK_val = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    ]
    BHK = models.CharField(max_length=10, choices=BHK_val)
    
    Buy_or_rent = [
        ('Buy', 'Buy'),
        ('Rent', 'Rent'),
    ]
    Avaliable_For = models.CharField(max_length=20, choices=Buy_or_rent)
    

    def __str__(self):
        return f"{self.PropertyName}"