from django.contrib import admin
from django.urls import path
from blog_app import views

urlpatterns = [
    path('about',views.AboutView.as_view(),name='about' ),
    path('',views.PostListView.as_view(),name='post_list'),
    path('post/{pk}',views.PostDetailView.as_view(),name='post_detail'),
    path('post/new',views.PostViewCreate.as_view(),name='post_new'),
    path('post/{pk}/edit',views.PostUpdateView.as_view(),name='post_edit'),
    path('post/{pk}/delete',views.PostDeleteView.as_view(),name='post_delete'),
    path('post/drafts',views.DraftListView.as_view(),name='post_drafts_list'),

]