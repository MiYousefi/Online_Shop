from django.urls import path

from .views import order_create_view

app_name = 'cart'
urlpatterns = [
    path('create/', order_create_view, name='order_create'),
]
