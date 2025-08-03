from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="home-page"),
    path("posts", views.PostsView.as_view(), name='posts-page', ),
    # This concept is called slug, /posts/first-post, /posts/second-post ...
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name='post-detail-page'),
    path("read-later", views.ReadLaterView.as_view(), name='read-later'),
]
