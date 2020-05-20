from django.shortcuts import render
from .models import Category, Tutorial


def tutorial_page(request):
    category = Category.objects.all()
    tutorials = Tutorial.objects.filter(is_draft=False)
    context = {
        'category': category,
        'tutorials': tutorials
    }
    return render(request, 'tutorial/tutorials.html', context)

def tutorial_details(request, tutorial_id):
    tutorial = Tutorial.objects.get(id=tutorial_id)
    ctg = Category.objects.get(name=tutorial.category)
    related_tutorial = Tutorial.objects.filter(category=ctg)
    context = {
        'tutorial': tutorial,
        'related_tutorial': related_tutorial,
        'categories':ctg
    }
    return render(request, 'tutorial/tutorial-details.html', context)

   

