from django.db import models
from user.models import User
from .post import PostModel


class Comments(models.Model):
    text = models.TextField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Rating(models.Model):
    LIKE = 'like'
    DISLIKE = 'dislike'

    RATING = [
        (LIKE, 'like'),
        (DISLIKE, 'dislike')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    reaction = models.CharField(max_length=7, choices=RATING)

    class Meta:
        unique_together = ("user", "post")