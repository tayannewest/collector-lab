from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Photocard, Style
from .forms import SoloForm
from django.views.generic import ListView, DetailView



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
  solo_form = SoloForm()
  return render(request, "photocards/detail.html", {"photocard": photocard, "solo_form": solo_form})

def add_solo(request, photocard_id):
  form = SoloForm(request.POST)
  if form.is_valid():
    new_solo = form.save(commit=False)
    new_solo.photocard_id = photocard_id
    new_solo.save()
  return redirect("photocards_detail", photocard_id=photocard_id)

class PhotocardCreate(CreateView):
  model = Photocard
  fields = "__all__"

class PhotocardUpdate(UpdateView):
  model = Photocard
  fields = ["band", "era", "description"]

class PhotocardDelete(DeleteView):
  model = Photocard
  success_url = "/photocards/"

class StyleCreate(CreateView):
  model = Style
  fields = "__all__"

class StyleList(ListView):
  model = Style

class StyleDetail(DetailView):
  model = Style

class StyleUpdate(UpdateView):
  model = Style
  fields = "__all__"

class StyleDelete(DeleteView):
  model = Style
  success_url = "/styles/"