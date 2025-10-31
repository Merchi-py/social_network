from django.db import models

from .components import Comments

from user.models import User


class BasePostModel(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    likes = models.IntegerField(null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.ForeignKey(Comments, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        abstract = True


class PostPhotoModel(BasePostModel):
    image = models.ImageField(upload_to='posts/', null=False)

class PostTextModel(BasePostModel):
    pass


