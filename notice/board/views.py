from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from models import Post, Comment
from forms import PostForm


def homepage(request):
    posts = Post.objects.order_by('-date')
    data = {
        'posts': posts
    }
    return render_to_response('homepage.html', data, context_instance=RequestContext(request))
