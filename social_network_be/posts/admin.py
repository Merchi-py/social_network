from django.contrib import admin
from .models import PostTextModel, PostPhotoModel, Comments
from user import models


admin.site.register(PostPhotoModel)
admin.site.register(PostTextModel)
admin.site.register(Comments)
admin.site.register(models.User)
