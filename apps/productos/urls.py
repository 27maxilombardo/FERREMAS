from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('productos/', views.productos, name='productos'),
    path('pedidos/', views.pedidos, name='pedidos'),
    path('pagos/', views.pagos, name='pagos'),
    path('contacto/', views.contacto, name='contacto'),
]
