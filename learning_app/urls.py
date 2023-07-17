from django.urls import path
from .views import (
    HomePageView,
    SubjectPageView,
    LearningPageView,
    DashboardPageView,
    AboutPageView,
    create_learning_item,
    update_completed,
)

urlpatterns = [
    path("learning/", LearningPageView.as_view(), name="learning"),
    #path("subject/", SubjectPageView.as_view(), name="subject"),
    path("dashboard/", DashboardPageView.as_view(), name="dashboard"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("", HomePageView.as_view(), name="home"),
    path("create/", create_learning_item, name="create_learning_item"),
    path("update/<int:item_id>/", update_completed, name="update_completed"),
]
