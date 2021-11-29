from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from .models import Photocard, Style, Photo
from .forms import SoloForm
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'photocardcollector'

# Create your views here.
class Home(LoginView):
  template_name = "home.html"

def about(request):
  return render(request, "about.html")

@login_required
def photocards_index(request):
  photocards = Photocard.objects.filter(user=request.user)
  return render(request, "photocards/index.html", { "photocards": photocards })

@login_required
def add_solo(request, photocard_id):
  form = SoloForm(request.POST)
  if form.is_valid():
    new_solo = form.save(commit=False)
    new_solo.photocard_id = photocard_id
    new_solo.save()
  return redirect("photocards_detail", photocard_id=photocard_id)

@login_required
def photocards_detail(request, photocard_id):
  photocard = Photocard.objects.get(id=photocard_id)
  styles_photocard_doesnt_have = Style.objects.exclude( id__in = photocard.styles.all().values_list("id"))
  solo_form = SoloForm()
  return render(request, "photocards/detail.html", {"photocard": photocard, "solo_form": solo_form, "styles": styles_photocard_doesnt_have})

class PhotocardCreate(LoginRequiredMixin, CreateView):
  model = Photocard
  fields = ["name", "band", "era", "description"]

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class PhotocardUpdate(LoginRequiredMixin, UpdateView):
  model = Photocard
  fields = ["band", "era", "description"]

class PhotocardDelete(LoginRequiredMixin, DeleteView):
  model = Photocard
  success_url = "/photocards/"

class StyleCreate(LoginRequiredMixin, CreateView):
  model = Style
  fields = "__all__"

class StyleList(LoginRequiredMixin, ListView):
  model = Style

class StyleDetail(LoginRequiredMixin, DetailView):
  model = Style

class StyleUpdate(LoginRequiredMixin, UpdateView):
  model = Style
  fields = "__all__"

class StyleDelete(LoginRequiredMixin, DeleteView):
  model = Style
  success_url = "/styles/"

@login_required
def assoc_style(request, photocard_id, style_id):
  Photocard.objects.get(id=photocard_id).styles.add(style_id)
  return redirect("photocards_detail", photocard_id=photocard_id)

@login_required
def add_photo(request, photocard_id):
  photo_file = request.FILES.get("photo-file", None)
  print(photo_file)
  if photo_file:
    s3 = boto3.client("s3")
    key = uuid.uuid4().hex + photo_file.name[photo_file.name.rfind("."):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, photocard_id=photocard_id)
      photocard_photo = Photo.objects.filter(photocard_id=photocard_id)
      if photocard_photo.first():
        photocard_photo.first().delete()
      photo.save()
    except Exception as err:
      print("An error occured uploading file to S3: %s" % err)
  return redirect("photocards_detail", photocard_id=photocard_id)

def signup(request):
  error_message = ""
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect("photocards_index")
    else:
      error_message = "Invalid sign up - try again"
  form = UserCreationForm()
  context = {"form": form, "error_message": error_message}
  return render(request, "signup.html", context)