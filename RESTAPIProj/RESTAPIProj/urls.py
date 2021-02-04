"""RESTAPIProj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin #for admin panel
from django.urls import path, include #for path and to include apps or routers urls.
from .router import router  #import router to connect through the url.
urlpatterns = [
    path('admin/', admin.site.urls), # This is used to access the admin panel of the website.
    path('', include("RESTAPIApp.urls")),
    path('api/', include(router.urls)),  #This will route the given url into router.urls file for generating the POST,GET and other request's.
]

#To access the json data API request will be like:- localhost:8000/api/employee