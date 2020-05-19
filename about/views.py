from django.shortcuts import render

# Create your views here.
def about_page(request):
    return render(request, 'about/about.html')

def map_page(request):
    return render(request, 'about/map.html')
