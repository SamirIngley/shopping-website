from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):

    title = models.CharField(max_length=100, unique=True, help_text='Title of your post.')
    author = models.ForeignKey(User, on_delete=models.PROTECT, help_text='The author of this post.')
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    last_modified = models.DateTimeField(auto_now=True)