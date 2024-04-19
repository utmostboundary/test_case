from django.urls import path

from cart import views

app_name = 'cart'

urlpatterns = [
    path('add-cart/', views.add_cart, name='add_cart')
]