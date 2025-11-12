from django.http import HttpResponseRedirect
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import PostModel
from .forms import PostCreationForm


class PostView(ListView):
    template_name = "posts/post_view.html"
    model = PostModel
    context_object_name = "text_posts"

    def get_queryset(self):
        return PostModel.objects.get_sorted_posts()

class PostCreateView(CreateView, LoginRequiredMixin):
    template_name = "posts/post_create.html"
    model = PostModel
    form_class = PostCreationForm
    success_url = "/"

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        return super().form_valid(form)


