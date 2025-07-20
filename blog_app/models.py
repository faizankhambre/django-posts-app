from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, unique=True)
    body = models.TextField(null=False, blank=False)
    slug = models.SlugField(default="default-slug", null=True)
    banner = models.ImageField(default="fallback.png", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"ID: {self.id} TITLE: {self.title} AUTHOR: {self.author}"
