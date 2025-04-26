from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_page, name="home-page"),
    path("posts", views.posts, name='posts-page', ),
    # This concept is called slug, /posts/first-post, /posts/second-post ...
    path("posts/<slug:slug>", views.post_detail, name='post-detail-page')
]
