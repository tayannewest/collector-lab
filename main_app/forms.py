from django.forms import ModelForm
from .models import Solo

class SoloForm(ModelForm):
  class Meta:
    model = Solo
    fields = ['date', 'title', 'genre']