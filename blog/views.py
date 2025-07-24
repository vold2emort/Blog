from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import ReviewForm
from django.views.generic import FormView
# Create your views here.


def index_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {'posts': latest_posts})


def posts(request):
    all_posts = Post.objects.all()
    return render(request, 'blog/all-post.html', {'all_posts': all_posts})


def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {'post': identified_post, "post_tags":identified_post.tags.all()})

class ReviewView(FormView):
    template_name = "blog/review.html"
    form_class = ReviewForm
    success_url = "home-page"

    def post(self, request):
        form = ReviewForm()
