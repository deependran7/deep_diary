from django.contrib import admin
from .models import Category, Article

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'date']

admin.site.register(Article, ProductAdmin)
admin.site.register(Category)
