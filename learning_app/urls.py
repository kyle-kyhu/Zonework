from django.urls import path
from .views import (
    HomePageView, 
    SubjectPageView,
    LearningPageView,
    DashboardPageView,
    AboutPageView,
)

urlpatterns = [
    path("<int:pk>/", LearningPageView.as_view(), name="learning"),
    path("subject/", SubjectPageView.as_view(), name="subject"),
    path("dashboard/", DashboardPageView.as_view(), name="dashboard"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("", HomePageView.as_view(), name="home"),
]