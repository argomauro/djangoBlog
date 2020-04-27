from django.shortcuts import render, get_object_or_404, redirect
from blog_app.models import Post, Comment
from blog_app.forms import CommentForm, PostForm
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator

from django.views.generic import (TemplateView, ListView, 
                                  CreateView, DetailView,
                                  UpdateView, DeleteView)

class AboutView(TemplateView):
    template_name = 'blog/about.html'
    
class PostListView(ListView):
    model = Post
    
    def get_queryset(self):
        return Post.objects.filter(publish_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post
    
class PostViewCreate(LoginRequiredMixin,CreateView):
    redirect_field_name='blog/post_detail.html'
    form_class = PostForm
    model = Post

class PostUpdateView(LoginRequiredMixin,UpdateView):
    redirect_field_name='blog/post_detail.html'
    form_class = PostForm
    model = Post

class PostDeleteView(LoginRequiredMixin, DeleteView):
    redirect_field_name='blog/post_list.html'
    model = Post
    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin, ListView):
    redirect_field_name='blog/post_list.html'
    model = Post
    
    def get_queryset(self):
        return Post.objects.filter(publish_date__isnull=True).order_by('created_date')
    

###########################################
###########################################
@login_required()
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = CommentForm()
    return render(request,'blog/comment_form.html')
    