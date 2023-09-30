from django.urls import path
from .views import (
    HomePageView,
    SubjectPageView,
    SessionPageView,
    DashboardPageView,
    AboutPageView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("subject/", SubjectPageView.as_view(), name="subject"),
    path("session", SessionPageView.as_view(), name="session"),
    path("dashboard/", DashboardPageView.as_view(), name="dashboard"),
    path("about", AboutPageView.as_view(), name="about"),
]
