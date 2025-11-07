from django.http import HttpResponseRedirect
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import PostModel
from .forms import PostCreationForm


class TextView(ListView):
    template_name = "posts/post_text.html"
    model = PostModel
    context_object_name = "text_posts"

class TextCreationView(CreateView):
    template_name = "posts/post_text_create.html"
    model = PostModel
    form_class = PostCreationForm
    success_url = "/"

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        return super().form_valid(form)


