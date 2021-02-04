from rest_framework import serializers  #use this serializers class to convert the model into json format.
from RESTAPIApp.models import Employee  #Database model class. 

class EmployeeSerializer(serializers.ModelSerializer):
    """
    1.Always give the serializer class name like:- yourmodelname + Serializer.
    2.serializers.ModelsSerializers in used to access the ModelSerializers.
    """
    class Meta:
        """
        This meta class is used to convert the data sent in a HTTP request to a Django object and a Django object to a valid response data.
        """
        model = Employee  #db model name.
        fields = '__all__'  #model fields.