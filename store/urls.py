
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.shop, name="shop"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('productdetail/', views.productdetail, name="productdetail"),

    path('update_item/', views.updateItem, name="updateItem"),
    path('process_order/', views.processOrder, name="processOrder"),

]
