from django.shortcuts import render
from .models import Photocard

# Create your views here.


def home(request):
  return render(request, "home.html")

def about(request):
  return render(request, "about.html")

def photocards_index(request):
  photocards = Photocard.objects.all()
  return render(request, "photocards/index.html", { "photocards": photocards })

def photocards_detail(request, photocard_id):
  photocard = Photocard.objects.get(id=photocard_id)
  return render(request, "photocards/detail.html", {"photocard": photocard})