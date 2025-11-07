from django.contrib import admin
from .models import PostModel, Comments
from user import models


admin.site.register(PostModel)
admin.site.register(Comments)
admin.site.register(models.User)
