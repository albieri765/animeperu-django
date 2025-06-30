# marketing/views.py
from django.shortcuts import render, redirect
from .forms import ContestForm
from .models import Contest
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt          # ⬅️ nuevo import

@csrf_exempt               # ⬅️ desactiva CSRF en este endpoint
@xframe_options_exempt     # permite que se cargue en <iframe>
def sorteo(request):
    if request.method == "POST":
        form = ContestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("gracias")
    else:
        form = ContestForm()
    return render(request, "marketing/sorteo.html", {"form": form})

def gracias(request):
    return render(request, "marketing/gracias.html")
def ver_participantes(request):
    participantes = Contest.objects.all().order_by('-id')
    return render(request, "marketing/participantes.html", {"participantes": participantes})