from django.db import models
from author.models import AuthorProfile
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='tutorial_category')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Tutorial(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='tutorials')
    details = RichTextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(AuthorProfile, on_delete=models.CASCADE)
    is_draft = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
