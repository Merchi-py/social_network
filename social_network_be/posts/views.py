from django.views.generic import ListView, TemplateView

from .models import PostTextModel, PostPhotoModel




class TextView(ListView):
    template_name = "posts/post_text.html"
    model = PostTextModel
    context_object_name = "text_posts"
