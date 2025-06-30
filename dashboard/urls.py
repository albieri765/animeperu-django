# dashboard/urls.py
from django.urls import path
from django.http import HttpResponse

def placeholder(request):
    return HttpResponse("Aquí irá tu dashboard pronto 🛠️")

urlpatterns = [
    path("", placeholder, name="dashboard_home"),
]
