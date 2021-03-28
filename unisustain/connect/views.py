from django.shortcuts import render, redirect

from .models import Post, Postcomment, User
from django.forms.models import model_to_dict


def get_all_posts(request):
    all_posts = list(Post.objects.all().values())
    for i in all_posts:
        i["username"] = User.objects.get(id=i["user_id"]).username
    context = {
        'all_posts':all_posts
    }
    return render(request, "connect/all_posts.html", context)

def get_post(request, post_id):
    query = Post.objects.get(postID = post_id)
    post = model_to_dict(query)
    post["username"] = User.objects.get(id=post["user"]).username
    try:
        all_comments = list(Postcomment.objects.filter(post = post_id).values())
        for i in all_comments:
            i["username"] = User.objects.get(id=i["user_id"]).username
    except Postcomment.DoesNotExist:
        all_comments = None
    context = {
        'post' : post,
        'all_comments' : all_comments
    }
    return render(request, "connect/post_view.html", context)

def create_post(request):
    if request.method == "POST":
        created_obj = Post.objects.get_or_create(
            title=request.POST.get('post_name'),
            content=request.POST.get('description'),
            tags=request.POST.get('tags'),
            search='Looking to Join',
            user_id=request.user.id,
        )
    return redirect("../")

def create_comment(request, post_id):
    if request.method == "POST":
        created_obj = Postcomment.objects.get_or_create(
            comment=request.POST.get('comment'),
            user_id=request.user.id,
            post_id=post_id,
        )
    query = Post.objects.get(postID = post_id)
    post = model_to_dict(query)
    post["username"] = User.objects.get(id=post["user"]).username
    try:
        all_comments = list(Postcomment.objects.filter(post = post_id).values())
        for i in all_comments:
            i["username"] = User.objects.get(id=i["user_id"]).username
    except Postcomment.DoesNotExist:
        all_comments = None
    context = {
        'post' : post,
        'all_comments' : all_comments
    }
    return render(request, "connect/post_view.html", context)
