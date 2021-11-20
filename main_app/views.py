from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
  return HttpResponse("<h1>Alright kweeb, time to out yourself</h1>")

def about(request):
  return HttpResponse("<h1>How about this parasocial weirdo am I right lmao</h1>")