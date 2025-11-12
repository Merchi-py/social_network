from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from posts.models import PostModel


class Profile(ListView, LoginRequiredMixin):
    template_name = "user/profile.html"
    model = PostModel
    context_object_name = "my_posts"

    def get_queryset(self):
        return PostModel.objects.get_sorted_posts(self.request.user)
