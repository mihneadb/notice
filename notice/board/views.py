from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from models import Post, Comment
from forms import PostForm


def homepage(request):
    posts = Post.objects.order_by('-date')
    data = {
        'posts': posts,
    }
    return render_to_response('homepage.html', data, context_instance=RequestContext(request))

@login_required
def post_add(request):
    if request.method == 'GET':
        form = PostForm()
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('homepage')

    data = {
        'form':form,
    }
    return render_to_response('post_add.html', data, context_instance=RequestContext(request))


@login_required
def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'GET':
        form = PostForm(instance=post)
    else:
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('homepage')

    data = {
        'form': form,
        'post': post,
    }
    return render_to_response('post_edit.html', data, context_instance=RequestContext(request))


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)

    data = {
        'post': post,
    }
    return render_to_response('post_detail.html', data, context_instance=RequestContext(request))


@login_required
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('homepage')

