from django.urls import path
from . import views 

urlpatterns = [
  path("", views.home, name="home"),
  path("about/", views.about, name="about"),
  path("photocards/", views.photocards_index, name="photocards_index"),
  path("photocards/<int:photocard_id>/", views.photocards_detail, name="photocards_detail"),
  path("photocards/create/", views.PhotocardCreate.as_view(),name="photocards_create"),
  path("photocards/<int:pk>/update/", views.PhotocardUpdate.as_view(), name="photocards_update"),
  path("photocards/<int:pk>/delete/", views.PhotocardDelete.as_view(), name="photocards_delete"),
  path("photocards/<int:photocard_id>/add_solo/", views.add_solo, name="add_solo"),
  path("styles/create/", views.StyleCreate.as_view(), name="styles_create"),
  path('styles/<int:pk>/', views.StyleDetail.as_view(), name='styles_detail'),
  path('styles/', views.StyleList.as_view(), name='styles_index'),
  path("styles/<int:pk>/update/", views.StyleUpdate.as_view(), name="styles_update"),
  path("styles/<int:pk>/delete/", views.StyleDelete.as_view(), name="styles_delete"),
  path('photocards/<int:photocard_id>/assoc_style/<int:style_id>/', views.assoc_style, name='assoc_style'),
]
