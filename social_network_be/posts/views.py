from django.http import HttpResponseRedirect
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

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
    success_url = reverse_lazy('home')


    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        return super().form_valid(form)


class PostDeleteView(DeleteView, LoginRequiredMixin):
    model = PostModel
    http_method_names = ['post']
    success_url = reverse_lazy('home')


class PostDetailView(DetailView, LoginRequiredMixin):
    template_name = 'posts/post_detail.html'
    model = PostModel
    slug_field = 'id'
    slug_url_kwarg = 'post_id'
    context_object_name = 'post'

# class PostUpdateView(UpdateView, LoginRequiredMixin):
#     template_name = "posts/post_update.html"
#     model = PostModel
