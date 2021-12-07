from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request) :
    return  render(request,"hello/index.html") 

def sourav(request) :
    return HttpResponse("Hare krishna sourav")

def alok(request) :
    return HttpResponse("hare krishna alok")

def nitesh(reqeust) :
    return HttpResponse("hare krishna nitesh")

def greet(request,name) :
    return render(request,"hello/greet.html",{
        "name" : name.capitalize()
    })

    # return HttpResponse(f"hare krishna {name.capitalize()}")



