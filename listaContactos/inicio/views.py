from django.shortcuts import render
from django.http import HttpResponse

def myHomeView(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html")

def anotherView(request):
    return HttpResponse("<h1>Solo otra pagina</h1>")

def informacionView(request):
    return HttpResponse("<h2>Acerca de Nosotros</h2><p>Esta es una página de información sobre nosotros.</p>")

def contactoView(request):
    return HttpResponse("<h2>Contacto</h2><p>Encuéntranos en Av. Venezuela N 725.</p>")

def productosView(request):
    return HttpResponse("<h2>Nuestros Productos</h2><p>Echa un vistazo a nuestra increíble selección de productos.</p>")
