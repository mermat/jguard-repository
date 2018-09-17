from django.urls import path

from blog.views import BlogListView
from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blog/', BlogListView.as_view(), name='blog'),
]
