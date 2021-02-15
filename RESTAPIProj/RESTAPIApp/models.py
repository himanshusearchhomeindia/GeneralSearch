from django.db import models

# Create your models here.


class PropertyList(models.Model):
    """
    This model will store the information about all the properties with their description and other information and we will use this model in general search.
    """
    Prop_ID = models.AutoField(
        primary_key=True)  # prop id will be our primary key.

    # property name will be stored here.
    PropertyName = models.CharField(max_length=60)

    # property images will get uploaded here.
    Property_Image = models.ImageField(upload_to='static/Property_images')

    # property price will be stored here.
    Property_Price = models.CharField(max_length=10)

    # property description will be stored here.
    Property_Description = models.TextField(max_length=180)

    PropertyStat = [
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed'),
        ('Ready to move', 'Ready to move'),
    ]  # choices for property status.
    # property status will be stored here.
    PropertyStatus = models.CharField(max_length=20, choices=PropertyStat)

    PropertyType = [
        ('Residential', 'Residentail'),
        ('Commercial', 'Commercial'),
    ]  # choices for propertytype.
    # property type will be stored here.
    Property_Type = models.CharField(
        max_length=20, choices=PropertyType, default='Residential')

    # builder name will get stored here.
    BuilderName = models.CharField(max_length=30)

    MultipleLocations = [
        ('Bangalore', 'Bangalore'),
        ('Mumbai', 'Mumbai'),
        ('Delhi', 'Delhi'),
        ('Punjab', 'Punjab'),
    ]  # choices for locations.
    # property locations will get stored here.
    Location = models.CharField(max_length=20, choices=MultipleLocations)

    # property address will get stored here.
    PropertyAddress = models.CharField(max_length=100)

    # property dimensions will get stored here.
    Area_in_sqft = models.CharField(max_length=20)

    BHK = models.CharField(max_length=20)  # BHK values will be stored here.

    # property avaliability will get stored here.
    Avaliable_For = models.CharField(max_length=8, default="Sale")

    def __str__(self):
        """
        This function will show the property name instead of object in admin panel.
        """
        return f"{self.PropertyName, self.Prop_ID}"


class PropertyImages(models.Model):

    """
    This model will store all the images of a particular property with the help of the ForeignKey(PropertyList)
    """
    Image_ID = models.ForeignKey(PropertyList, on_delete=models.CASCADE)  #image id will be based in Foreign key.
    Images = models.ImageField(upload_to='static/IndividualPropImgs')  #here the multiple images will get stored !(one image at a time).

    def __str__(self):
        """
        This function will show the property name instead of object in admin panel.
        """
        return f"{self.Image_ID}"
