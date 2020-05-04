from django.contrib import admin
from blog_app import models
# Register your models here.
#admin.site.register(models.Comment)
#admin.site.register(models.Post)

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ('author', 'publish_date')
    search_fields = ('author','title')
    prepopulated_fields = {'text': ('title',)}
    raw_id_fields = ('author',)
    
@admin.register(models.Comment)
class PostAdmin(admin.ModelAdmin):
    list_filter = ('author', 'post__title')
    raw_id_fields = ('post',)