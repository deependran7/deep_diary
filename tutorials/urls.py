from django.urls import path
from . import views

urlpatterns = [
    path('', views.tutorial_page, name='tutorial'),
    path('tutorial/<tutorial_id>', views.tutorial_details, name='t_details'),
    
    
]
