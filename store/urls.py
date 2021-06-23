
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.main, name="main"),
    path('store/', views.store, name="store"),
    path('checkout/', views.checkout, name="checkout"),
]