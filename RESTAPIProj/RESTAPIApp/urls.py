from django.urls import path#for accessing the path of view functions.
from RESTAPIApp import views #for accessing the index page.
urlpatterns = [
    path('', views.home, name='home'), #this will show the home page.
]