from django.contrib import admin
from .models import Category, Tutorial

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'date']

admin.site.register(Tutorial, ProductAdmin)
admin.site.register(Category)
