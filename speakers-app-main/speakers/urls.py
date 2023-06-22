from django.urls import path
from . import views

urlpatterns = [
    path("", views.speakers_list, name="speakers_list"),
    path("<int:pk>/", views.speaker_detail, name="speaker_detail"),
]