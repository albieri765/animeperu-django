from django.urls import path
from . import views

urlpatterns = [
    path("sorteo/", views.sorteo, name="sorteo"),
    path("gracias/", views.gracias, name="gracias"),
]