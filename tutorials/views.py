from django.shortcuts import render
from .models import Category, Article


def tutorials_page(request):
    category = Category.objects.all()
    articles = Article.objects.filter(is_draft=False)
    context = {
        'category': category,
        'articles': articles
    }
    return render(request, 'shop/shop.html', context)

def article_details(request, article_id):
    article = Article.objects.get(id=article_id)
    ctg = Category.objects.get(name=article.category)
    related_article = Article.objects.filter(category=ctg)
    context = {
        'article': article,
        'related_article': related_article
    }
    return render(request, 'shop/product-details.html', context)


