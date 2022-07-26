from django.shortcuts import render
from .models import Food
# Create your views here.
def menu(request):
    foods = Food.objects.all()
    context = {
        # 'cuisine':cuisine
        'foods':foods
    }
    return render(request,'food/menu.html', context)

def details(request, id):
    food = Food.objects.get(id=id)
    context = {
        'food' :food
    }
    return render(request, 'food/details.html', context)