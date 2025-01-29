from django.db import models
from django.conf import settings
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager
from django.contrib.auth.models import User


class Post(models.Model):
    h1 = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    description = RichTextUploadingField()
    content = RichTextUploadingField()
    image = models.ImageField()
    created_at = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=5.99)
    tags = TaggableManager()

    def __str__(self):
        return self.title

