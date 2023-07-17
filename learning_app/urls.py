from django.urls import path
from .views import (
    HomePageView,
    SubjectPageView,
    #LearningPageView,
    LearningPageView2,
    DashboardPageView,
    AboutPageView,
)

urlpatterns = [
    path("learning/", LearningPageView2.as_view(), name="learning"),
    path("subject/", SubjectPageView.as_view(), name="subject"),
    path("dashboard/", DashboardPageView.as_view(), name="dashboard"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("", HomePageView.as_view(), name="home"),
]
