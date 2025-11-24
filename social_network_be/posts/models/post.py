from django.db import models

from user.models import User

from base.models import TimeStampedModel

from .components import Comments
from posts.managers import PostManager, SortedProfilePosts


class PostModel(TimeStampedModel, models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/', null=True, blank=True)

    likes = models.IntegerField(null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.ForeignKey(Comments, on_delete=models.CASCADE, blank=True, null=True)

    objects = PostManager()
    profile = SortedProfilePosts()





