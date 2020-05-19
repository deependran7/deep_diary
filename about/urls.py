from django.urls import path
from .views import about_page, map_page

urlpatterns = [
    path('', map_page, name='about')
    #path('mappage/', map_page, name = 'map_page')
]
