from django.shortcuts import render #This is used to render the home page.
from .serializers import PropertyListSerializer #This is used to get the PropertyListSerializer class to convert it into python obj to json obj. 
from .models import PropertyList #by using this model we will do the filteration of the properties.
from rest_framework.response import Response #this is used to send the response into the API request.
from rest_framework.decorators import api_view #we are using the function based views in RESTapi for this we need this decorator class.

# Create your views here.
def home(request):
    """
    This will return the index page.
    """
    return render(request, 'index.html')

@api_view(['POST']) #decorator with POST request permission.
def PropertyView(request):
    """
    This function will access the searchquery from the API request and do the filteration with the database and in the end return the response.
    """
    SearchQuery = request.data['SearchQuery']  #accessing the searchquery form the API request.
    PropertyTypeQuery = request.data['PropertyTypeQuery']  #accessing the PropertyTypeQuery form the API request.
    LocationQuery = request.data['LocationQuery']  #accessing the LocationQuery form the API request.
    
    PropertyName = PropertyList.objects.filter(PropertyName__icontains = SearchQuery) #filter the properties which matches the searchquery with the property name.
    PropertyDescription = PropertyList.objects.filter(Property_Description__icontains = SearchQuery).filter(Property_Description__icontains = LocationQuery)  #filter the properties which matches the SearchQuery and LocationQuery with the property descritpion.
    PropertyLocation = PropertyList.objects.filter(Location__icontains = LocationQuery)  #filter the properties which matches the LocationQuery with the property location.
    PropertyStatus = PropertyList.objects.filter(PropertyStatus__icontains = SearchQuery)  #filter the properties which matches the SearchQuery with the property status.
    Property_Type = PropertyList.objects.filter(Property_Type__icontains = PropertyTypeQuery)  #filter the properties which matches the PropertyQuery with the property type.
    BuilderName = PropertyList.objects.filter(BuilderName__icontains = SearchQuery)  #filter the properties which matches the SearchQuery with the builders name.
    
    #testing
    # print("propertyname",PropertyName)
    # print("Property desc",PropertyDescription)
    # print("property loc",PropertyLocation)
    # print("property stat",PropertyStatus)
    # print("property typ",Property_Type)
    # print("builder name",BuilderName)

    #Multiple filters for getting the exact output.
    NormalFilter = PropertyName.intersection(PropertyDescription, PropertyLocation, Property_Type, PropertyStatus, BuilderName)  #making a intersection from all the matched data into one with only one similar properties.   
    
    Filter_Location = PropertyLocation.union(NormalFilter)  #union function to get the location based results from NormalFilter.
    
    Filter_Prop_type = Property_Type.intersection(Filter_Location)  #intersection function to get results based on the property type from Filter_Location.
    
    FinalResult = PropertyName.intersection(Filter_Prop_type) #intersection function to get results based on the property name form the Filter_Prop_type.

    #testing
    # print(FinalResult)

    serializer = PropertyListSerializer(FinalResult, many=True) #serializing the data into json format.
    return Response(serializer.data) #sending the results back to the API request.