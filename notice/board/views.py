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