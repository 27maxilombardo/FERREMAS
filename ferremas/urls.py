# ferremas/urls.py
from django.contrib import admin
from django.urls import path, include  # Importa include para incluir las URLs de otras apps

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.productos.urls')),  # Asegúrate de incluir las URLs de productos
]
