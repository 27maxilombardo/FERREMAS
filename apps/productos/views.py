from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def productos(request):
    return render(request, 'productos.html')

def pedidos(request):
    return render(request, 'pedidos.html')

def pagos(request):
    return render(request, 'pagos.html')

def contacto(request):
    return render(request, 'contacto.html')
