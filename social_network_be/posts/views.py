from django.db import transaction
from django.http import JsonResponse
from django.views.generic import ListView, TemplateView, DetailView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import F

from .models import PostModel, Comments, Rating
from .forms import PostCreationForm, PostUpdateForm


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


class PostUpdateView(UpdateView, LoginRequiredMixin):
    template_name = "posts/post_update.html"
    model = PostModel
    slug_field = 'id'
    slug_url_kwarg = 'post_id'

    def get_form_class(self):
        return PostUpdateForm

    def get_object(self, queryset=None):
        return PostModel.objects.get(id=self.kwargs["post_id"], user=self.request.user)

    def get_success_url(self):
        return reverse_lazy("detail_post", kwargs={"post_id": self.object.id})


class LikeSystem(View, LoginRequiredMixin):
    http_method_names = ["post"]

    def post(self, request, *args, **kwargs):
        post_id = self.kwargs["post_id"]
        user = request.user

        post = PostModel.objects.get(id=post_id)


        with transaction.atomic():
            rating = Rating.objects.filter(user=user, post=post).first()


            #first click on button
            if rating is None:
                Rating.objects.create(user=user, post=post, reaction=Rating.LIKE)
                PostModel.objects.filter(id=post_id).update(likes_count=F("likes_count") + 1)


            # If user clicked on the Button second time
            elif rating.reaction == Rating.LIKE:
                rating.delete()
                PostModel.objects.filter(id=post_id).update(likes_count=F("likes_count") - 1)


            #from dislike to like
            else:
                rating.reaction = Rating.LIKE
                rating.save(update_fields=["reaction"])
                PostModel.objects.filter(id=post_id).update(
                    likes_count=F("likes_count") + 1,
                    dislikes_count=F("dislikes_count") - 1)

        # Return new Values
        new_value = PostModel.objects.values("likes_count", "dislikes_count").get(id=post_id)
        return JsonResponse({'response': new_value})


class DisLikeSystem(View, LoginRequiredMixin):
    http_method_names = ["post"]

    def post(self, request, *args, **kwargs):
        post_id = self.kwargs["post_id"]
        user = request.user

        post = PostModel.objects.get(id=post_id)


        with transaction.atomic():
            rating = Rating.objects.filter(user=user, post=post).first()

            # If user clicks on the Dislike Button
            if rating is None:
                Rating.objects.create(user=user, post=post, reaction=Rating.DISLIKE)
                PostModel.objects.filter(id=post_id).update(dislikes_count=F("dislikes_count") + 1)

            #if user clicks again on the button
            elif rating.reaction == Rating.DISLIKE:
                rating.delete()
                PostModel.objects.filter(id=post_id).update(dislikes_count=F("dislikes_count") - 1)

            # on click, from like to dislike
            else:
                rating.reaction = Rating.DISLIKE
                rating.save(update_fields=["reaction"])
                PostModel.objects.filter(id=post_id).update(
                    dislikes_count=F("dislikes_count") + 1,
                    likes_count=F("likes_count") - 1)

        # Return new Values
        new_values = PostModel.objects.values("dislikes_count", "likes_count").get(id=post_id)
        return JsonResponse({'response': new_values})


