from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class Category(models.Model):
    """
    Model to store blog category.
    """
    name = models.CharField(max_length=50)
    created_on = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    Model to store blog post.
    """

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=90)
    description = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title