from django.urls import path
from django.http import HttpResponse

def pendiente(request):
    return HttpResponse("🔧 Gestor de productos en construcción")

urlpatterns = [
    path("", pendiente, name="manager_home"),
]
