from django.urls import path#for accessing the path of view functions.
from RESTAPIApp import views #for accessing the index page and propertyview function.
urlpatterns = [
    path('', views.home, name='home'), #this will show the home page.
    path('properties/', views.PropertyView, name='PropertyView'), #This is the API url from where the user will send its API request and get the json data.
]