from django.http import HttpResponse
from django.shortcuts import render #this one use to return from the templates folder 

def home_view(request):
    user = request.user
    hello = "HI IAM JARVIS"

    content = {  #define a dicitonary
       'user' : user ,#key:value , which we get from models.py
       'hello' : hello ,
    }
    return render(request, 'main/home.html', content)
    #return HttpResponse('JARViS')