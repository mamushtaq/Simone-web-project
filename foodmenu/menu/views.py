from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Dish

# Create your views here.
list_empty = True

def menu (request):
    return render(request, 'menu/menu.html', {
        'dishes' : Dish.objects.all(),
    })

def cart (request):
    list_empty = True
    for dish in Dish.objects.all():
        if dish.added_to_cart:
            list_empty = False
    return render(request, 'menu/cart.html', {
        'dishes' : Dish.objects.all(),
        'list_empty' : list_empty
    })

def add(request, dish_name):
    Dish.objects.filter(name=dish_name).update(added_to_cart=True)
    return render(request, 'menu/menu.html', {
        'dishes' : Dish.objects.all()
    })

def remove(request, dish_name):
    Dish.objects.filter(name=dish_name).update(added_to_cart=False)
    return render(request, 'menu/cart.html', {
        'dishes' : Dish.objects.all()
    })
        
