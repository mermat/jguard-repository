from django.urls import path

from .views import HomeView
    # ContactView

urlpatterns = [
    path(r'', HomeView.as_view(), name='home'),
]
