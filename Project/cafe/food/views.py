from django.shortcuts import render
from .models import Cuisine
# Create your views here.
def menu(request):
    cuisine = Cuisine.objects.all()
    context = {
        'cuisine':cuisine
    }
    return render(request,'food/menu.html', context)