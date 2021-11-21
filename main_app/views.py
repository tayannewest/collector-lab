from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

class PhotocardCreate(CreateView):
  model = Photocard
  fields = "__all__"

class PhotocardUpdate(UpdateView):
  model = Photocard
  fields = ["band", "era", "description"]

class PhotocardDelete(DeleteView):
  model = Photocard
  success_url = "/photocards/"