from django.contrib import admin
from .models import Photocard, Solo, Style, Photo

# Register your models here.
admin.site.register(Photocard)
admin.site.register(Solo)
admin.site.register(Style)
admin.site.register(Photo)