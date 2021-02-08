#REST API + JSON data parse into HTML table.

##Steps.

1.created a virtual environment in python.
2.install djangorestframework.
3.create a djangoproject:- RESTAPIProj.
4.create a djangoapp:- RESTAPIApp.
5.added RESTAPIApp and 'rest_framework' in settings.py.(RESTAPIProj)
6.created a database in postgressql with pgadmin4.
7.Added database details in settings.py file.(RESTAPIProj)
8.make migrtions then migrate.
9.Created a db model PropertyList in models.py.(RESTAPIApp)
10.again make migrations and migarte.
11.created serializers.py file and written the code.(RESTAPIApp)
12.add code in urls.py.(RESTAPIProj)
13.Created template and static folder.
14.added template in settings.py file.(RESTAPIProj)
15.added html file in template folder and javascript file in static folder.(RESTAPIApp)
16.created urls.py and views.py. (RESTAPIApp)
17.test the complete project.

##Testing
-To access the json data use the url- http://127.0.0.1:8000/properties/
-To access the page use:- (RESTENV) PS D:\REST-API-Proj\RESTAPI-SearchFunction\RESTAPIProj> python manage.py runserver
-Admin panel:- username = himanshu
password = himanshu