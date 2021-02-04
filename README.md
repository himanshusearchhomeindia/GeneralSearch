#REST API + JSON data parse into HTML table.

##Steps.

1.created a virtual environment in python.
2.install djangorestframework.
3.create a djangoproject:- RESTAPIProj.
4.create a djangoapp:- RESTAPIApp.
5.added RESTAPIApp and 'rest_framework' in settings.py.(RESTAPIProj)
6.created a database in postgressql with pgadmin3.
7.Added database details in settings.py file.(RESTAPIProj)
8.make migrtions then migrate.
9.Created a db model Employee in models.py.(RESTAPIApp)
10.again make migrations and migarte.
11.created serializers.py file and written the code.(RESTAPIApp)
12.created viewsets.py and written the code.(RESTAPIApp)
13.created routers.py and written the code.(RESTAPIApp)
14.add code in urls.py.(RESTAPIProj)
15.Created template and static folder.
16.added template in settings.py file.(RESTAPIProj)
17.added html file in template folder and javascript file in static folder.(RESTAPIApp)
19.created urls.py and views.py. (RESTAPIApp)
20.test the complete project.

##Testing
-To access the json data use the url- http://127.0.0.1:8000/api/employee/
-To access the page use:- (RESTAPI) PS E:\companyProject\REST_API-project\RESTAPIProj> python manage.py runserver