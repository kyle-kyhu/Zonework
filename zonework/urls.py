from django.urls import path

from .views import (
    SubjectListView,
    SubjectDetailView,
    DashboardView,  
)


urlpatterns = [
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("<int:pk>/", SubjectDetailView.as_view(), name="subject_detail"),
    path("", SubjectListView.as_view(), name="subject_list"),
]