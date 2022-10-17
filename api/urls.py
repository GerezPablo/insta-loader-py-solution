from django.urls import path, re_path
from . import views

urlpatterns = [
    path("api/", views.root, name="root"),
    re_path(r'^api/download/(?P<shortCode>[A-Za-z0-9\-\_]*)$',
            views.downloadPost, name="downloadPost"),
]
