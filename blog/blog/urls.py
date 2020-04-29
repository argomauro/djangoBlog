from django.contrib import admin
from django.urls import path, include
from blog_app import views as blogview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog_app.urls')),
    path('', blogview.dashboard, name='dashboard'),


]
