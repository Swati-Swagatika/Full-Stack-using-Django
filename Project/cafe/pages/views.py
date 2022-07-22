from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    # return HttpResponse("<h1> Hello World! </h1>")
    return render(request,'pages/index.html')

def about(request):
    x = 10
    y = -20 
    foods =['Tea', 'Coffee', 'Pepsi']
    students = {
        'Tom': 80,
        'Jerry': 45,
        'Casper': 47,
        'Spike' : 75
    }
    context = {        #predefined dictionary
        'x': x,
        'y': y,
        'foods':foods,
        'students':students,
    }
   
    return render(request,'pages/about.html',context)
    
def contact(request):
    return render(request, 'pages/contact.html')
