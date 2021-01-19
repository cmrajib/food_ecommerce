from django import template
from taggit.models import Tag

from blog.models import Category, Post

register = template.Library()

@register.simple_tag(name="categories")
def all_categories():
    return Category.objects.all()

@register.simple_tag(name="tags")
def all_tags():
    return Tag.objects.all()


@register.simple_tag(name="recent_posts")
def all_post():
    return Post.objects.order_by('-created')[:5]


# @register.simple_tag(name="hit_posts")
# def hit_posts():
#     return Post.objects.order_by('-hit')[:5]