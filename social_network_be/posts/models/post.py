from django.db import models

from .components import Likes, Comments

from user.models import User


class PostModel(models.Model):
    title = models.CharField(max_length=50)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.ForeignKey(Comments, on_delete=models.CASCADE)
    likes = models.ForeignKey(Likes, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
