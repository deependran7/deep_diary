from django.shortcuts import render
from contact.forms import SubscriberForm
from tutorials.models import Tutorial

def home_page(request):
    tutorial= Tutorial.objects.latest('id')
    
    forms = SubscriberForm()
    if request.method == 'POST':
        forms = SubscriberForm(request.POST)
        if forms.is_valid():
            forms.save()
    context = {
        
        'forms': forms,
        'tutorial':tutorial
    }
    return render(request, 'home.html', context)
