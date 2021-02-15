from django.db.models.fields.files import ImageField
from django.shortcuts import render  # This is used to render the home page.
# This is used to get the PropertyListSerializer class to convert it into python obj to json obj.
from .serializers import PropertyListSerializer
# by using this model we will do the filteration of the properties.
from .models import PropertyList, PropertyImages
# this is used to send the response into the API request.
from rest_framework.response import Response
# we are using the function based views in RESTapi for this we need this decorator class.
from rest_framework.decorators import api_view

# Create your views here.


def home(request):
    """
    This will return the index page.
    """
    return render(request, 'index.html')

def PropertyListing(request):
    """
    This page will show the property listing page to the user.
    """
    return render(request, 'listing-1 actual.html')

@api_view(['POST'])  # decorator with POST request permission.
def PropertyView(request):
    """
    This function will access the searchquery from the API request and do the filteration with the database and in the end return the response.
    """
    SearchQuery = request.data['SearchQuery']  # accessing the searchquery form the API request.
    # accessing the PropertyTypeQuery form the API request.
    PropertyTypeQuery = request.data['PropertyTypeQuery']
    # accessing the LocationQuery form the API request.
    LocationQuery = request.data['LocationQuery']

    # filter the properties which matches the searchquery with the property name.
    PropertyName = PropertyList.objects.filter(
        PropertyName__icontains=SearchQuery)
    # filter the properties which matches the SearchQuery and LocationQuery with the property descritpion.
    PropertyDescription = PropertyList.objects.filter(
        Property_Description__icontains=SearchQuery).filter(Property_Description__icontains=LocationQuery)
    # filter the properties which matches the LocationQuery with the property location.
    PropertyLocation = PropertyList.objects.filter(
        Location__icontains=LocationQuery)
    # filter the properties which matches the SearchQuery with the property status.
    PropertyStatus = PropertyList.objects.filter(
        PropertyStatus__icontains=SearchQuery)
    # filter the properties which matches the PropertyQuery with the property type.
    Property_Type = PropertyList.objects.filter(
        Property_Type__icontains=PropertyTypeQuery)
    # filter the properties which matches the SearchQuery with the builders name.
    BuilderName = PropertyList.objects.filter(
        BuilderName__icontains=SearchQuery)

    # Multiple filters for getting the exact output.
    # making a intersection from all the matched data into one with only one similar properties.
    NormalFilter = PropertyName.intersection(
        PropertyDescription, PropertyLocation, Property_Type, PropertyStatus, BuilderName)

    # union function to get the location based results from NormalFilter.
    Filter_Location = PropertyLocation.union(NormalFilter)

    # intersection function to get results based on the property type from Filter_Location.
    Filter_Prop_type = Property_Type.intersection(Filter_Location)

    # intersection function to get results based on the property name form the Filter_Prop_type.
    FinalResult = PropertyName.intersection(Filter_Prop_type)

    if len(FinalResult) != 0:
        # serializing the data into json format.
        serializer = PropertyListSerializer(FinalResult, many=True)
        print(serializer.data)
        # sending the results back to the API request.
        return Response(serializer.data)
    else:
        # intersection function to get results based on the property type from Filter_Location.
        FinalResult = Property_Type.intersection(Filter_Location)
        # serializing the data into json format.
        print(FinalResult)
        serializer = PropertyListSerializer(FinalResult, many=True)
        # sending the results back to the API request.
        return Response(serializer.data)


def IndividualProp(request, Prop_ID):
    """
    This function access the Prop_ID form the url and with the help 
    of that Prop_ID it will filter out the individual property details as well as the multiple images of the particular property from the
    PropertyList model.
    """
    Ind_PropData = PropertyList.objects.filter(Prop_ID__icontains=Prop_ID)  # Filtering the individual prop data by using the Prop_ID.
    Ind_Prop_Images = PropertyImages.objects.filter(Image_ID= Prop_ID)  #Filter the images according to the Ind_PropData.
    Ind_PropDataDict = {
        'Prop_Data': Ind_PropData,
        'Prop_Img': Ind_Prop_Images,
    }  # Creating the Prop_Data dictionary to send it in the front end template.
    return render(request, 'IndividualProp.html', Ind_PropDataDict)
