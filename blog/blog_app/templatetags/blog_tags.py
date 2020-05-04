from django import template
from ..models import Post

register = template.Library()
@register.simple_tag(name='numero_posts')
def total_posts():
    return Post.objects.all().count()