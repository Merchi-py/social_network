from django.db import models
from datetime import datetime, timedelta


class SortedProfilePostsQuerySet(models.QuerySet):

    def get_posts_by_user(self, user):
        return self.filter(user=user)

    def get_new_posts(self, user):
        two_days_ago = datetime.now() - timedelta(days=2)
        return self.get_posts_by_user(user).filter(created_at__gt=two_days_ago)

    def get_sorted_posts(self, user):
        return self.get_new_posts(user).order_by("-created_at")


class SortedProfilePosts(models.Manager):

    def get_queryset(self):
        return SortedProfilePostsQuerySet(self.model, using=self._db)

    def get_posts_by_user(self, user):
        return self.get_queryset().get_posts_by_user(user)

    def get_new_posts(self, user):
        return self.get_queryset().get_new_posts(user)

    def get_sorted_posts(self, user):
        return self.get_queryset().get_sorted_posts(user)
