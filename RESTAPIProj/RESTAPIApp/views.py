from django.db.models import query
from django.shortcuts import render
from .serializers import PropertyListSerializer
from .models import PropertyList
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
def home(request):
    """
    This will return the index page.
    """
    return render(request, 'index.html')

@api_view(['POST'])
def PropertyView(request):
    SearchQuery = request.data['SearchQuery']
    # Results = []
    
    PropertyName = PropertyList.objects.filter(PropertyName__icontains = SearchQuery)
    PropertyDescription = PropertyList.objects.filter(Property_Description__icontains = SearchQuery)
    PropertyLocation = PropertyList.objects.filter(Location__icontains = SearchQuery)
    PropertyStatus = PropertyList.objects.filter(PropertyStatus__icontains = SearchQuery)
    Property_Type = PropertyList.objects.filter(Property_Type__icontains = SearchQuery)
    BuilderName = PropertyList.objects.filter(BuilderName__icontains = SearchQuery)
    
    Results = PropertyName.union(PropertyDescription, PropertyLocation, PropertyStatus, Property_Type, BuilderName)

    serializer = PropertyListSerializer(Results, many=True)
    return Response(serializer.data)