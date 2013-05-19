from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from models import Post, Comment, Category
from forms import PostForm, CommentForm


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
    form = CommentForm()

    comments = post.comment_set.order_by('-date').all()

    data = {
        'post': post,
        'form': form,
        'comments': comments,
    }
    return render_to_response('post_detail.html', data, context_instance=RequestContext(request))


@login_required
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('homepage')


@login_required
def comment_add(request, id):
    post = get_object_or_404(Post, id=id)
    form = CommentForm(request.POST)
    if form.is_valid():
        text = form.cleaned_data['text']
        comment = Comment(text=text, author=request.user, post=post)
        comment.save()
    return redirect('post_detail', id)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('homepage')
    else:
        form = UserCreationForm()
    data = {
        'form': form,
    }
    return render_to_response('register.html', data, context_instance=RequestContext(request))


def category_list(request, id):
    category = get_object_or_404(Category, id=id)
    posts = category.post_set.order_by('-date').all()

    data = {
        'posts': posts,
        'category': category,
    }

    return render_to_response('category.html', data, context_instance=RequestContext(request))


def categories(request):
    categories = Category.objects.order_by('name').all()

    data = {
        'categories': categories,
    }
    return render_to_response('categories.html', data, context_instance=RequestContext(request))

