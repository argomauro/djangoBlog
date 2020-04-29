from django.contrib import admin
from django.urls import path, include
from blog_app import views as blogview
from django.conf.urls import (handler400, handler403, handler404, handler500)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog_app.urls')),
    path('', blogview.dashboard, name='dashboard'),
]
handler400= 'blog_app.views.handler404'