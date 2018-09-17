from django.views import generic

from .models import Post


class BlogListView(generic.ListView):
    """
    to list advertisements under a particular category
    """
    model = Post
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'

    # def get_queryset(self, **kwargs):
    #     slug = self.kwargs['slug']
    #     post = Post.objects.get(slug=slug)
    #     ads = Advertisement.objects.filter(category=category)
    #     return ads