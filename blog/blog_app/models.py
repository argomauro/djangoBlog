from django.db import models
from django.utils import timezone
from django.urls import path, reverse, reverse_lazy
from django.contrib import admin

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.publish_date = timezone.now()
        self.save()
    
    def approve_comments(self):
        #restituisce tutti i commenti approvati leggendo
        #la relazione che è definita a livello di Comment
        return self.approve_comments.filter(approved_comments=True)
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    
    
    def __str__(self):
        return self.title + ' - ' +self.author.name    


class Comment(models.Model):
    post = models.ForeignKey('blog_app.Post', related_name='comments', on_delete=models.DO_NOTHING)
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    approved_comments = models.BooleanField(default=False)

    def approve(self):
        self.approved_comments = True
        self.save()
        
    def get_absolute_url(self):
        return reverse("post_list")
    
    def __str__(self):
        return self.text