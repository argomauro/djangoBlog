from django.contrib import admin
from django.urls import path
from blog_app import views
from django.contrib.auth import views as auth_views

app_name = 'blog'
urlpatterns = [
    path('about',views.AboutView.as_view(),name='about' ),
    path('post/list',views.PostListView.as_view(),name='post_list'),
    path('post/{pk}',views.PostDetailView.as_view(),name='post_detail'),
    path('post/new',views.PostViewCreate.as_view(),name='post_new'),
    path('post/{pk}/edit',views.PostUpdateView.as_view(),name='post_edit'),
    path('post/{pk}/delete',views.PostDeleteView.as_view(),name='post_delete'),
    path('post/drafts',views.DraftListView.as_view(),name='post_drafts_list'),
    path('post/{pk}/comment',views.add_comment_to_post,name='add_comment_to_post'),
    path('comment/{pk}/approve',views.comment_approve,name='comment_approve'),
    path('comment/{pk}/delete',views.comment_remove,name='comment_remove'),
    path('post/{pk}/publish',views.post_publish,name='post_publish'),
    path('accounts/login', auth_views.LoginView.as_view(),name='login'),
    path('accounts/logout', auth_views.LogoutView.as_view(), name='logout',kwargs={'next_page':'dashboard'}),
    path('', views.dashboard, name='dashboard'),

]