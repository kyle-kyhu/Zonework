from django.urls import path

from .views import AddVideoView

urlpatterns = [
    path("add_video/", AddVideoView.as_view(), name="add_video"),
]