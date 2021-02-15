from django.contrib import admin
from .models import PropertyList  #importing the model for registration in admin account.
from .models import PropertyImages  #importing the model for registration in admin account.
# Register your models here.
admin.site.register(PropertyList)  #model registered.
admin.site.register(PropertyImages)  #model registered.