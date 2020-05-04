from django.shortcuts import render, get_object_or_404, redirect
from blog_app.models import Post, Comment
from blog_app.forms import CommentForm, PostForm
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.core.mail import send_mail
from taggit.models import Tag
from django.contrib import messages

from django.views.generic import (TemplateView, ListView, 
                                  CreateView, DetailView,
                                  UpdateView, DeleteView)

class AboutView(TemplateView):
    template_name = 'about.html'
    
class PostListView(ListView):
    model = Post
    paginate_by = 2
    def get_queryset(self):
        qs = super().get_queryset()
        return qs


class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(LoginRequiredMixin,CreateView):
    template_name = 'post_form.html'
    form_class = PostForm


class PostUpdateView(LoginRequiredMixin,UpdateView):
    redirect_field_name='post_form.html'
    model = Post
    fields = '__all__'


class PostDeleteView(LoginRequiredMixin, DeleteView):
    #redirect_field_name='post_list.html'
    model = Post
    success_url = reverse_lazy('blog_app:post_list')

class DraftListView(LoginRequiredMixin, ListView):
    template_name='post_drafts_list.html'
    model = Post
    paginate_by = 2

    
    def get_queryset(self):
        qs = super().get_queryset().filter(publish_date__isnull=True).order_by('create_date')
        print('Elementi trovati: ' + str(qs.count()))
        return qs
    
    

###########################################
###########################################
@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog_app:post_detail',pk=post.pk)
    else:
        form = CommentForm()
    return render(request,'comment_form.html',{'form':form})



@login_required   
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    messages.info(request, 'Commento approvato con successo')
    return redirect('blog_app:post_detail',pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blog_app:post_detail',pk=post_pk)

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    #INVIAMO LA EMAIL DI CONFERMA PUBBLICAZIONE
    messages.info(request, 'Post pubblicato con successo')
    send_mail('subjetc','Messagio','margoneto@publisys.it',('maurizio.argoneto@gmail.com',), fail_silently=True)
    return redirect('blog_app:post_detail', pk=pk)

def dashboard(request):
    return render(request, 'registration/dashboard.html', {'section':'dashboard'})


# HTTP Error 400
def handler404(request, exception):
    return render(request, 'blog_app/404.html', locals())