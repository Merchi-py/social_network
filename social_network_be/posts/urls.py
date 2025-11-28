"""
URL configuration for social_network_be project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *

urlpatterns = [
    path("", PostView.as_view(), name="home"),
    path("create-post/", PostCreateView.as_view(), name="create_post"),
    path("delete-post/<int:pk>/", PostDeleteView.as_view(), name="delete_post"),
    path("detail-post/<int:post_id>/", PostDetailView.as_view(), name="detail_post"),
    path("update-post/<int:post_id>/", PostUpdateView.as_view(), name="update_post"),
    path("like_system/<int:post_id>/", LikeSystem.as_view(), name="like_system"),
    path("dislike_system/<int:post_id>/", DisLikeSystem.as_view(), name="dislike_system"),
    path("create-comment/<int:post_id>/", CommentCreate.as_view(), name="create_comment")

]

