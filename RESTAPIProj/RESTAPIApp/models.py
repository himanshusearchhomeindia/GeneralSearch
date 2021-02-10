from django.db import models

# Create your models here.
class PropertyList(models.Model):
    """
    This model will store the information about all the properties with their description and other information and we will use this model in general search.
    """
    Prop_ID = models.AutoField(primary_key=True) #prop id will be our primary key.

    PropertyName = models.CharField(max_length=60) #property name will be stored here.
    
    Proprety_Image = models.ImageField(upload_to = 'static/Property_images') #property images will get uploaded here.
    
    Property_Price = models.CharField(max_length=10)  #property price will be stored here.
    
    Property_Description = models.TextField(max_length=180) #property description will be stored here.
    
    PropertyStat = [
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed'),
        ('Ready to move', 'Ready to move'),
    ] #choices for property status.
    PropertyStatus = models.CharField(max_length=20, choices=PropertyStat) #property status will be stored here.
    
    PropertyType = [
        ('Residential', 'Residentail'),
        ('Commercial', 'Commercial'),
    ] #choices for propertytype.
    Property_Type = models.CharField(max_length=20, choices=PropertyType, default='Residential') #property type will be stored here.

    BuilderName = models.CharField(max_length=30) #builder name will get stored here.
    
    MultipleLocations = [
        ('Bangalore', 'Bangalore'),
        ('Mumbai', 'Mumbai'),
        ('Delhi', 'Delhi'),
        ('Punjab', 'Punjab'),
    ] #choices for locations.
    Location = models.CharField(max_length=20, choices=MultipleLocations) #property locations will get stored here.
    
    PropertyAddress = models.CharField(max_length=100) #property address will get stored here.
    
    Area_in_sqft = models.CharField(max_length=20) #property dimensions will get stored here.
    
    BHK_val = [
        ('1bhk', '1bhk'),
        ('2bhk', '2bhk'),
        ('3bhk', '3bhk'),
        ('4bhk', '4bhk'),
    ] #choices for BHK's
    BHK = models.CharField(max_length=10, choices=BHK_val) #BHK values will be stored here.
    
    Buy_or_rent = [
        ('Buy', 'Buy'),
        ('Rent', 'Rent'),
    ] #choices for avaliability.
    Avaliable_For = models.CharField(max_length=20, choices=Buy_or_rent) #property avaliability will get stored here.
    

    def __str__(self):
        """
        This function will show the property name instead of object in admin panel.
        """
        return f"{self.PropertyName}"