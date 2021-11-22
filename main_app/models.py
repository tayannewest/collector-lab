from django.db import models
from django.urls import reverse

# Create your models here.

SOLOS = (
  ("D", "Dance/Pop"),
  ("B", "Ballad"),
  ("R", "Rap"),
)

class Photocard(models.Model):
  name = models.CharField(max_length=100)
  band = models.CharField(max_length=100)
  era = models.CharField(max_length=100)
  description = models.TextField(max_length=250)

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