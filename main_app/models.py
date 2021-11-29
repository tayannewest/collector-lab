from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

SOLOS = (
  ("D", "Dance/Pop"),
  ("B", "Ballad"),
  ("R", "Rap"),
)

class Style(models.Model):
  clothing = models.CharField(max_length = 50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.clothing

  def get_absolute_url(self):
      return reverse("styles_detail", kwargs={"pk": self.id})
  

class Photocard(models.Model):
  name = models.CharField(max_length=100)
  band = models.CharField(max_length=100)
  era = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  styles = models.ManyToManyField(Style)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse("photocards_detail", kwargs={"photocard_id": self.id})


class Solo(models.Model):
  date = models.DateField("Release date")
  title = models.CharField(max_length=100)
  genre = models.CharField(
    max_length=1,
    choices=SOLOS,
    default=SOLOS[0][0]
    )

  photocard = models.ForeignKey(Photocard, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.title} is a {self.get_genre_display} song released on {self.date}"

  class Meta:
    ordering = ["-date"]

  def solo_for_today(self):
    return self.solo_set.filter(date=date.today().count() >= len(SOLOS))

class Photo(models.Model):
  url = models.CharField(max_length=250)
  photocard = models.OneToOneField(Photocard, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for photocard_id: {self.photocard_id} @{self.url}"