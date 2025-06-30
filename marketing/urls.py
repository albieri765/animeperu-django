from django.urls import path
from . import views

urlpatterns = [
    path("", views.sorteo, name="sorteo_root"),   # ← esta línea nueva
    path("sorteo/", views.sorteo, name="sorteo"),
    path("gracias/", views.gracias, name="gracias"),
    path("participantes/", views.ver_participantes, name="ver_participantes"),
]