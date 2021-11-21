from django.urls import path
from . import views 

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("photocards/", views.photocards_index, name="photocards_index"),
    path("photocards/<int:photocard_id>/", views.photocards_detail, name="photocards_detail"),
    path("photocards/create/", views.PhotocardCreate.as_view(), name="photocards_create"),
    path("photocards/<int:pk>/update/", views.PhotocardUpdate.as_view(), name="photocards_update"),
    path("photocards/<int:pk>/delete/", views.PhotocardDelete.as_view(), name="photocards_delete"),
    
]
