from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse, reverse_lazy
from blog_app.models import Post

class LatestEntriesFeed(Feed):
    title = "Ultimi post del Blog"
    link = reverse_lazy('blog_app:post_list')
    description = "Aggiornamenti in tempo reale dei Post del nostro meraviglioso Blog"

    def items(self):
        return Post.objects.filter(publish_date__isnull=False).order_by('publish_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.text,30)