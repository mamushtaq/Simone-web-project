from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .models import Dish
from django.urls import reverse
import email, imaplib
import socket
socket.getaddrinfo('localhost', 8080)

# From here is code to retrieve email

user_address = 'simootest1998@gmail.com'
user_password = 'Djangoproject1998'

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(user_address, user_password)
mail.select('inbox')

def parse_email(request):
    result, data = mail.uid('search', None, "ALL")
    i = data[0].split()
    most_recent = i[-1]
    result2, email_data = mail.uid('fetch', most_recent, '(RFC822)')
    raw_email = email_data[0][1].decode("utf-8")
    email_message = email.message_from_string(raw_email)
    for part in email_message.walk():
        if part.get_content_type() == "text/plain":
            body = part.get_payload(decode=True)
            body = body.decode('utf-8')
            list_of_menu = []
            term = ""
            for alphabet in body:
                if alphabet == ":":
                    list_of_menu.append(term)
                    term = ""
                    continue
                elif alphabet == "\n":
                    continue
                else:
                    term = term + alphabet
            not_price = True
            for dishes in Dish.objects.all():
                dishes.delete()
            for word in list_of_menu:
                if not_price:
                    name_of_dish = word
                    not_price = False
                else:
                    price_of_dish = word
                    added = False
                    q = 1
                    dish = Dish.objects.create(name = name_of_dish, price = price_of_dish, added_to_cart = added, quantity = q)
                    dish.save()
                    not_price = True

            return HttpResponseRedirect(reverse("menu"))
        else:
            pass



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

def add(request, dish_id):
    dish = Dish.objects.get(id = dish_id)
    dish.added_to_cart = True
    dish.save()
    return HttpResponseRedirect(reverse("menu"))

def remove(request, dish_id):
    Dish.objects.filter(id=dish_id).update(added_to_cart=False)
    return HttpResponseRedirect(reverse("cart"))

def change(request, dish_id):
    if request.method == "POST":
        new_quantity = request.POST["quantity"]
        Dish.objects.filter(id=dish_id).update(quantity = new_quantity)
        return HttpResponseRedirect(reverse("cart"))

def send_list(request):
    list_of_dishes = "Dishes\tQuantity\n"
    for dishes in Dish.objects.all():
        if dishes.added_to_cart:
            list_of_dishes += f"{dishes.name}\t{dishes.quantity}\n"
            Dish.objects.filter(id=dishes.id).update(added_to_cart=False)
    send_mail(
        'Order',
        list_of_dishes,
        settings.EMAIL_HOST_USER,
        ['restobrendaservice@gmail.com'],
        fail_silently=False
    )
    return HttpResponseRedirect(reverse("cart"))
    
    
    
        
