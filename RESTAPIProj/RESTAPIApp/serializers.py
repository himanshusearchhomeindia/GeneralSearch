from rest_framework import serializers  #use this serializers class to convert the model into json format.
from RESTAPIApp.models import PropertyList  #Database model class. 

class PropertyListSerializer(serializers.ModelSerializer):
    """
    1.Always give the serializer class name like:- yourmodelname + Serializer.
    2.serializers.ModelsSerializers in used to access the ModelSerializers.
    """
    class Meta:
        """
        This meta class is used to convert the data sent in a HTTP request to a Django object and a Django object to a valid response data.
        """
        model = PropertyList  #db model name.
        fields = '__all__'  #model fields here i am selecting all the fields.