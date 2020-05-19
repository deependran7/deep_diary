from django.urls import path
from . import views

urlpatterns = [
    path('', views.tutorials_page, name='tutorial'),
    path('tutorial/<article_id>', views.article_details, name='tut_details'),
    
]
