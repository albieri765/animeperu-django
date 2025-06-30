
from django.shortcuts import render, redirect
from .forms import ContestForm
from django.views.decorators.clickjacking import xframe_options_exempt  # ⬅️ nuevo import

@xframe_options_exempt   # ⬅️ añade este decorador
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
