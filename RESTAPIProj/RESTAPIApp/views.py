from django.shortcuts import render #used for rendering the html page.

# Create your views here.
def home(request):
    """
    This will return the index page.
    """
    return render(request, 'index.html')