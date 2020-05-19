from django.shortcuts import render
from contact.forms import SubscriberForm

def home_page(request):
    
    forms = SubscriberForm()
    if request.method == 'POST':
        forms = SubscriberForm(request.POST)
        if forms.is_valid():
            forms.save()
    context = {
        
        'forms': forms
    }
    return render(request, 'home.html', context)
