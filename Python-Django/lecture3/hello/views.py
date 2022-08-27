from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# request is the hhtp request the user make to get access to the web server
def index(request): 
    #return HttpResponse("Hello world!")
    return render(request=request, template_name="hello/index.html")

def nick(request): 
    return HttpResponse("Hello Nick")

# Parametrised function
def greet(request, name: str): 
    return render(
        request=request, 
        template_name="hello/greet.html", 
        # context is a dict with keys to pass to the temaplates, which it will be able to use 
        context={
            "name": name.capitalize()
    })