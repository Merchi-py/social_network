from django.db import models

from .components import Likes, Comments

from user.models import User


class BasePostModel(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.ForeignKey(Comments, on_delete=models.CASCADE)
    likes = models.ForeignKey(Likes, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

class PostPhotoModel(BasePostModel):
    image = models.ImageField(upload_to='posts/', null=False)

class PostTextModel(BasePostModel):
    pass

