from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from posts.models import PostModel
from .models import User
from .forms import UserUpdateForm

class Profile(ListView, LoginRequiredMixin):
    template_name = "user/profile.html"
    model = PostModel
    context_object_name = "my_posts"

    def get_queryset(self):
        return PostModel.profile.get_sorted_posts(self.request.user)

class ProfileEdit(UpdateView, LoginRequiredMixin):
    template_name = "user/profile_edit.html"
    model = User
    slug_field = 'id'
    slug_url_kwarg = 'user_id'
    form_class = UserUpdateForm
    success_url = reverse_lazy("profile")


