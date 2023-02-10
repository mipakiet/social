from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import AddPost, AddComment


def post(request, post_id):

    if request.method == 'POST':
        comment_form = AddComment(request.POST)
        if comment_form.is_valid():
            comment_object = comment_form.save(commit=False)
            comment_object.author = request.user
            comment_object.post = Post.objects.get(id=post_id)
            print(type(comment_object))
            comment_object.save()

            return redirect(post, post_id=post_id)
    else:
        comment_form = AddComment()

    post_object = Post.objects.get(id=post_id)
    liked = False
    if post_object.likes.filter(id=request.user.id).exists():
        liked = True

    comment_objects = Comment.objects.filter(post__id=post_id).order_by("pub_date")

    context = {
        'post_is_liked': liked,
        'post': post_object,
        'comment_form': comment_form,
        'comment_objects': comment_objects,
    }

    return render(request, "post.html", context)


def posts(request):
    posts_objects = Post.objects.all().order_by("-pub_date")
    context = {
        'posts': posts_objects,
    }

    return render(request, "posts.html", context)


@login_required
def add_post(request):
    if request.method == 'POST':
        form = AddPost(request.POST)
        if form.is_valid():
            post_object = form.save(commit=False)
            post_object.author = request.user
            post_object.save()

            return redirect(post, post_id=post_object.id)
    else:
        form = AddPost()

    context = {
        'form': form,
    }

    return render(request, "add_post.html", context)


def delete_post(request, post_id):

    post_object = Post.objects.get(id=post_id)
    post_object.delete()

    return redirect(posts)


def like_post(request, post_id):

    post_object = Post.objects.get(id=post_id)
    if post_object.likes.filter(id=request.user.id).exists():
        post_object.likes.remove(request.user)
    else:
        post_object.likes.add(request.user)

    return redirect(post, post_id=post_id)
