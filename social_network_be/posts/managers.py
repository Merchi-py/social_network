from django.db import models
from datetime import datetime, timedelta


class PostQuerySet(models.QuerySet):

    def get_new_posts(self):
        two_days_ago = datetime.now() - timedelta(days=2)
        return self.filter(created_at__gt=two_days_ago)

    def get_sorted_posts(self):
        return self.get_new_posts().order_by("-created_at")


class PostManager(models.Manager):

    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def get_new_posts(self):
        return self.get_queryset().get_new_posts()

    def get_sorted_posts(self):
        return self.get_queryset().get_sorted_posts()


class SortedProfilePosts(models.Manager):

    def get_queryset(self, user):
        return PostQuerySet(self.model, using=self._db).filter(user=user)


    def get_sorted_posts(self, user):
        return self.get_queryset(user).get_sorted_posts()
