from django.db import models
from user.models import User


class Likes(models.Model):
    count = models.BigIntegerField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Comments(models.Model):
    text = models.TextField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)

