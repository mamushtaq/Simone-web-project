from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.menu, name="menu"),
    path("your_cart", views.cart, name="cart"),
    path("<str:dish_id>/add", views.add, name="add"),
    path("<str:dish_id>/remove", views.remove, name="remove"),
    path("<str:dish_id>/change", views.change, name="change"),
    path("getmenu", views.parse_email, name="getmenu"),
    path("sendlist", views.send_list, name="sendlist")
]