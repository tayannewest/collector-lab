from django.shortcuts import render

# Create your views here.

class Photocard:
  def __init__(self, name, band, era, description):
    self.name = name
    self.band = band
    self.era = era
    self.description = description

photocards = [
  Photocard("Suga", "BTS", "HYYH", "Loved the pastel hair in this era, what a look"),
  Photocard("Moonbyul", "Mamamoo", "White Wind", "The suits were everything, Moonbyul is for the gays"),
  Photocard("Taemin", "SHINee", "Lucifer", "It's nice to know that South Korea didn't escape the iron grip of a scene phase"),
  Photocard("Felix", "Stray Kids", "Back Door", "Such pretty, feminine styling on such a deep-voiced boy"),
]

def home(request):
  return render(request, "home.html")

def about(request):
  return render(request, "about.html")

def photocards_index(request):
  return render(request, "photocards/index.html", { "photocards": photocards })