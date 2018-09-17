from django import template

from blog.models import *

register = template.Library()


@register.simple_tag
def post_list():
    post_list = Post.objects.all()
    return post_list


@register.simple_tag
def category_list():
    category_list = Category.objects.all()
    print("FFFFFFF",category_list)
    return category_list
