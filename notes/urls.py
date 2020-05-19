from django.urls import path
from . import views


urlpatterns = [
    path('', views.Notes, name='Notes'),

    path('upload/', views.UploadNotes, name='UploadNotes'),




 ]
