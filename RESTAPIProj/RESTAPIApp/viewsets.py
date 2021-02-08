# from rest_framework import viewsets  #import viewsets from rest_framework
# from RESTAPIApp import models  #import db models
# from RESTAPIApp import serializers  #import serializer for conversion.
# # from rest_framework.decorators import api_view
# from rest_framework.response import Response

# class PropertyListViewset(viewsets.ModelViewSet):
#     """
#     1.Always give the viewset class name like:- yourmodelname + Viewset.
#     2.viewsets.ModelViewSet in used to access the ModelViewSet.

#     A ViewSet class is simply a type of class-based View, that does not provide any method handlers such as .get() or .post(), and instead provides actions such as .list() and .create().
#     """
#     def propertysearch(self, request):
#         if request.method == 'POST':
#             queryset = models.PropertyList.objects.all()  #access all the objects of the Employee model.
#             serializer_class = serializers.PropertyListSerializer(queryset)  #access the EmployeeSerializer.
#             return Response(serializer_class.data)


#it will create classes like list(), retrive(), update(), destroy().