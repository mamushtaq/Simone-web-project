from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.menu, name="menu"),
    path("your_cart", views.cart, name="cart"),
    path("<str:dish_name>/add", views.add, name="add"),
    path("<str:dish_name>/remove", views.remove, name="remove")
]