from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):

    title = models.CharField(max_length=100, unique=True, help_text='Title of your post.')
    author = models.ForeignKey(User, on_delete=models.CASCADE, help_text='The author of this post.') # if a user is deleted, their posts get deleted too
    description = models.TextField(help_text='Description of your post.')

    date_posted = models.DateTimeField(default=timezone.now)   # date posted now modifiable with 'default' field
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    