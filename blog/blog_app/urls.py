from django.contrib import admin
from django.urls import path
from blog_app import views
from django.contrib.auth import views as auth_views

app_name = 'blog_app'
urlpatterns = [
    path('about',views.AboutView.as_view(),name='about' ),
    path('post/list',views.PostListView.as_view(),name='post_list'),
    path('post/drafts',views.DraftListView.as_view(),name='post_drafts_list'),
    path('post/<int:pk>',views.PostDetailView.as_view(),name='post_detail'),
    path('post/create',views.PostCreateView.as_view(),name='post_create'),
    path('post/<int:pk>/edit',views.PostUpdateView.as_view(),name='post_edit'),
    path('post/<int:pk>/delete',views.PostDeleteView.as_view(),name='post_delete'),
    path('post/<int:pk>/comment',views.add_comment_to_post,name='add_comment_to_post'),
    path('comment/<int:pk>/approve',views.comment_approve,name='comment_approve'),
    path('comment/<int:pk>/delete',views.comment_remove,name='comment_remove'),
    path('post/<int:pk>/publish',views.post_publish,name='post_publish'),
    path('accounts/login', auth_views.LoginView.as_view(),name='login'),
    path('accounts/logout', auth_views.LogoutView.as_view(), name='logout',kwargs={'next_page':'dashboard'}),
    path('', views.dashboard, name='dashboard'),

]